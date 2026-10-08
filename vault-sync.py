"""Local vault dashboard. Standard library only; preview fetches without changing notes."""
import argparse
import hashlib
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import secrets
import subprocess
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = Path(__file__).resolve().parent
VAULT = 'chatgpt-to-obsidian/utkarsh-vault/'
REMOTE = 'https://github.com/unknown77master/utkarsh-obsidian-mem.git'
IST = timezone(timedelta(hours=5, minutes=30))


def commit_message(paths, now=None):
    now = (now or datetime.now(IST)).astimezone(IST)
    month = 'jan feb mar apr may jun jul aug sep oct nov dec'.split()[now.month - 1]
    context = ', '.join(Path(p).stem for p in paths[:3])
    if len(paths) > 3:
        context += f' and {len(paths) - 3} more vault files'
    context = ' '.join(context.replace('(', '[').replace(')', ']').split())[:180]
    return (f'{now.day:02d}-{month}-{now.year}:{now.hour % 12 or 12}-{now.minute:02d}:'
            f'{"AM" if now.hour < 12 else "PM"} (updated {context})')


class Sync:
    def __init__(self, root=ROOT, interval=120, read_only=False):
        self.root, self.interval, self.read_only = Path(root), interval, read_only
        self.guard = threading.Lock()
        self.wake = threading.Event()
        self.paused = False
        self.state = dict(status='Starting', last_attempt=None, last_success=None,
                          next_check=None, branch=None, upstream=None, pending=[],
                          ahead=0, behind=0, error=None, events=[])

    def git(self, *args):
        env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='Never')
        result = subprocess.run(['git', '-C', str(self.root), *args], env=env,
                                capture_output=True, timeout=60)
        if result.returncode:
            raise RuntimeError(f'git {args[0]} failed: ' + result.stderr.decode('utf-8', 'replace').strip()[-1200:])
        return result.stdout.decode('utf-8', 'surrogateescape').strip('\n')

    def event(self, message):
        entry = dict(time=datetime.now(IST).isoformat(timespec='seconds'), message=message)
        self.state['events'] = (self.state['events'] + [entry])[-60:]
        try:
            folder = self.root / '.vault-sync'
            folder.mkdir(exist_ok=True)
            log = folder / 'activity.log'
            if log.exists() and log.stat().st_size > 1_000_000:
                log.replace(folder / 'activity.previous.log')
            with log.open('a', encoding='utf-8') as stream:
                stream.write(json.dumps(entry, ensure_ascii=True) + '\n')
        except OSError:
            pass

    def paths(self, *args):
        return [p for p in self.git(*args, '-z').split('\0') if p]

    def changes(self):
        return sorted(set(self.paths('diff', '--name-only', '--no-renames') +
                          self.paths('ls-files', '--others', '--exclude-standard')))

    def protected(self, path):
        return path.startswith(VAULT + 'Raw/Export/') or Path(path).name in {
            '.export-mirror-manifest.json', '.chatgpt-migration-state.json'}

    def fingerprint(self, paths):
        digest = hashlib.sha256()
        for name in paths:
            digest.update(name.encode('utf-8', 'surrogateescape'))
            path = self.root / name
            if path.is_symlink():
                raise RuntimeError(f'Symlink needs manual review: {name}')
            digest.update(path.read_bytes() if path.exists() else b'<deleted>')
        return digest.hexdigest()

    def git_path(self, name):
        path = Path(self.git('rev-parse', '--git-path', name))
        return path if path.is_absolute() else self.root / path

    def synchronize(self, paths, remote, ahead, behind):
        if self.state['branch'] != 'main':
            raise RuntimeError('Automatic sync requires main.')
        if self.git('config', 'branch.main.merge') != 'refs/heads/main':
            raise RuntimeError('Configure main to track the remote main branch.')
        if any(self.git_path(name).exists() for name in ('MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'rebase-merge', 'rebase-apply', 'index.lock')):
            raise RuntimeError('A Git operation is in progress; resolve it manually.')
        if self.paths('diff', '--name-only', '--diff-filter=U'):
            raise RuntimeError('Unresolved Git conflicts need manual review.')
        if self.paths('diff', '--cached', '--name-only'):
            raise RuntimeError('Staged work exists; finish it manually before syncing.')
        if any(not p.startswith(VAULT) or self.protected(p) for p in paths):
            raise RuntimeError('Unrelated or protected files changed; review and commit them manually.')
        if any(not (self.root / p).exists() for p in paths):
            raise RuntimeError('Vault deletions require manual review and commit.')
        incoming = self.paths('diff', '--name-only', '--no-renames', 'HEAD...@{upstream}')
        if any(self.protected(p) for p in incoming):
            raise RuntimeError('Incoming protected export changes require manual review.')
        # Inspect every outgoing commit, including files removed again in later commits.
        outgoing = self.git('log', '--format=', '--name-only', '--no-renames', '@{upstream}..HEAD').splitlines()
        if any(p and (not p.startswith(VAULT) or self.protected(p)) for p in outgoing):
            raise RuntimeError('Outgoing commits include non-vault or protected changes; push them manually.')
        if paths:
            before = self.fingerprint(paths)
            time.sleep(3)
            if paths != self.changes() or before != self.fingerprint(paths):
                self.state['status'] = 'Waiting for edits to settle'
                return
            self.git('add', '--', *paths)
            staged = self.paths('diff', '--cached', '--name-only', '--no-renames')
            if sorted(staged) != paths:
                raise RuntimeError('Index changed during sync; staged work retained for review.')
            if before != self.fingerprint(paths):
                self.git('reset', '--quiet', 'HEAD', '--', *paths)
                self.state['status'] = 'Waiting for edits to settle'
                return
            message = commit_message(paths)
            self.git('commit', '-m', message)
            self.event(message)
        if self.changes() or self.paths('diff', '--cached', '--name-only'):
            raise RuntimeError('New edits appeared during sync; retry once edits settle.')
        if behind:
            try:
                self.git('pull', '--rebase', remote, 'main')
            except Exception as error:
                if any(self.git_path(p).exists() for p in ('rebase-merge', 'rebase-apply')):
                    self.git('rebase', '--abort')
                raise RuntimeError(f'Pull failed; local commits retained. Resolve manually. {error}') from error
            self.event('Pulled remote memory updates')
        if self.git('rev-list', '--count', '@{upstream}..HEAD') != '0':
            self.git('push', remote, 'HEAD:refs/heads/main')
            self.event('Pushed local memory updates')
        self.state.update(status='Up to date', pending=[], ahead=0, behind=0,
                          last_success=datetime.now(IST).isoformat(timespec='seconds'))

    def cycle(self):
        if not self.guard.acquire(blocking=False):
            return
        try:
            self.state.update(status='Checking', error=None, last_attempt=datetime.now(IST).isoformat(timespec='seconds'))
            self.state['branch'] = self.git('branch', '--show-current') or '(detached)'
            self.state['pending'] = sorted(set(self.paths('diff', 'HEAD', '--name-only', '--no-renames') + self.paths('ls-files', '--others', '--exclude-standard')))
            self.state['upstream'] = self.git('rev-parse', '--abbrev-ref', '@{upstream}')
            remote = self.git('config', f'branch.{self.state["branch"]}.remote')
            if self.git('remote', 'get-url', remote) != REMOTE or self.git('remote', 'get-url', '--push', remote) != REMOTE:
                raise RuntimeError('Remote must match the authorized private memory repository.')
            self.git('fetch', remote)
            ahead, behind = map(int, self.git('rev-list', '--left-right', '--count', 'HEAD...@{upstream}').split())
            self.state.update(ahead=ahead, behind=behind)
            if self.read_only:
                self.state.update(status='Preview only', last_success=datetime.now(IST).isoformat(timespec='seconds'))
                self.event(f'Checked memory: {ahead} local / {behind} remote commits ahead')
            else:
                self.synchronize(self.changes(), remote, ahead, behind)
        except Exception as error:
            self.state.update(status='Needs attention', error=str(error))
            self.event(str(error))
        finally:
            self.state['next_check'] = time.time() + self.interval
            self.guard.release()

    def worker(self):
        while True:
            if not self.paused:
                self.cycle()
            self.wake.wait(self.interval)
            self.wake.clear()


def lock_instance(root):
    folder = root / '.vault-sync'
    folder.mkdir(exist_ok=True)
    stream = (folder / 'service.lock').open('a+b')
    stream.seek(0)
    stream.write(b'0')
    stream.flush()
    stream.seek(0)
    try:
        if os.name == 'nt':
            import msvcrt
            msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        stream.close()
        raise RuntimeError('The vault dashboard is already running.')
    return stream


def serve(sync, port):
    token = secrets.token_urlsafe(32)
    page = (ROOT / 'vault-sync-dashboard.html').read_text(encoding='utf-8').replace('__TOKEN__', token)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def reply(self, code, body, content_type='application/json'):
            data = body.encode('utf-8')
            self.send_response(code)
            self.send_header('Content-Type', content_type + '; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Frame-Options', 'DENY')
            self.end_headers()
            self.wfile.write(data)

        def allowed(self):
            return self.headers.get('Host') in {f'127.0.0.1:{port}', f'localhost:{port}'}

        def do_GET(self):
            if not self.allowed():
                self.reply(403, '{}')
            elif self.path == '/':
                self.reply(200, page, 'text/html')
            elif self.path == '/api/status':
                self.reply(200, json.dumps(dict(sync.state, paused=sync.paused, busy=sync.guard.locked(),
                           interval=sync.interval, read_only=sync.read_only, repository=str(sync.root)), ensure_ascii=True))
            else:
                self.reply(404, '{}')

        def do_POST(self):
            if not self.allowed() or self.headers.get('X-Sync-Token') != token:
                self.reply(403, '{}')
                return
            if self.path == '/api/pause':
                sync.paused = True
                sync.event('Paused; an active check will finish safely')
            elif self.path == '/api/resume':
                sync.paused = False
                sync.wake.set()
                sync.event('Resumed checks')
            elif self.path == '/api/sync':
                if sync.paused:
                    self.reply(409, '{}')
                    return
                sync.wake.set()
            elif self.path == '/api/stop':
                sync.paused = True
                sync.event('Stopping after active cycle finishes')
                def stop_safely():
                    with sync.guard:
                        server.shutdown()
                threading.Thread(target=stop_safely, daemon=True).start()
            else:
                self.reply(404, '{}')
                return
            self.reply(200, '{}')

    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    threading.Thread(target=sync.worker, daemon=True).start()
    print(f'Vault dashboard: http://127.0.0.1:{port}', flush=True)
    server.serve_forever()
    server.server_close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--interval', type=int, default=120)
    parser.add_argument('--once', action='store_true')
    parser.add_argument('--read-only', action='store_true', help='Fetch and preview; never commit, pull or push')
    args = parser.parse_args()
    if args.interval < 10:
        parser.error('Interval must be at least 10 seconds.')
    instance_lock = lock_instance(ROOT)
    try:
        sync = Sync(interval=args.interval, read_only=args.read_only)
        if args.once:
            sync.cycle()
            print(json.dumps(sync.state, indent=2))
            return 1 if sync.state['error'] else 0
        serve(sync, args.port)
    finally:
        instance_lock.close()


if __name__ == '__main__':
    raise SystemExit(main())
