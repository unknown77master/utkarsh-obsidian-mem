"""Git calls are simulated: these tests never create commits or send vault data."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from datetime import datetime
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('vault_sync', Path(__file__).parents[1] / 'vault-sync.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FakeSync(module.Sync):
    def __init__(self, root, pending=(), staged=(), behind=0, read_only=False):
        super().__init__(root, read_only=read_only)
        self.pending, self.staged = list(pending), list(staged)
        self.behind = behind
        self.ahead = 0
        self.commands = []
        self.conflict = False
        self.rebasing = False
        self.outgoing = ''

    def git(self, *args):
        self.commands.append(args)
        if args[:2] == ('branch', '--show-current'): return 'main'
        if args[:2] == ('rev-parse', '--abbrev-ref'): return 'origin/main'
        if args[0] == 'config': return 'refs/heads/main' if args[1].endswith('.merge') else 'origin'
        if args[0] == 'remote': return module.REMOTE
        if args[:2] == ('rev-parse', '--git-path'):
            name = args[-1]
            path = self.root / '.git' / name
            if self.rebasing and name == 'rebase-merge': path.mkdir(parents=True, exist_ok=True)
            return str(path)
        if args[0] == 'rev-list':
            return f'{self.ahead}\t{self.behind}' if '--left-right' in args else str(self.ahead)
        if args[0] == 'log': return self.outgoing
        if args[0] == 'diff':
            if '--cached' in args: return '\0'.join(self.staged)
            if '--diff-filter=U' in args or 'HEAD...@{upstream}' in args: return ''
            return '\0'.join(self.pending)
        if args[0] == 'ls-files': return ''
        if args[0] == 'add': self.staged = list(args[2:])
        if args[0] == 'commit':
            self.staged.clear(); self.pending.clear(); self.ahead += 1
        if args[0] == 'pull' and self.conflict:
            self.rebasing = True
            raise RuntimeError('simulated conflict')
        if args[0] == 'rebase': self.rebasing = False
        if args[0] == 'push': self.ahead = 0
        return ''


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.note = module.VAULT + 'Projects/Note.md'
        path = self.root / self.note
        path.parent.mkdir(parents=True)
        path.write_text('validated context', encoding='utf-8')

    def tearDown(self): self.temp.cleanup()

    def run_cycle(self, sync):
        with patch.object(module.time, 'sleep'):
            sync.cycle()
        return [c[0] for c in sync.commands]

    def test_commit_format_and_ist(self):
        now = datetime(2026, 10, 6, 2, 58, tzinfo=module.IST)
        self.assertEqual(module.commit_message([self.note], now), '06-oct-2026:2-58:AM (updated Note)')
        self.assertIn(':12-00:AM ', module.commit_message([self.note], now.replace(hour=0, minute=0)))
        self.assertIn(':12-58:PM ', module.commit_message([self.note], now.replace(hour=12)))

    def test_local_update_commit_then_pull_then_push(self):
        sync = FakeSync(self.root, pending=[self.note], behind=1)
        commands = self.run_cycle(sync)
        self.assertLess(commands.index('commit'), commands.index('pull'))
        self.assertLess(commands.index('pull'), commands.index('push'))
        self.assertEqual(sync.state['status'], 'Up to date')
        self.assertEqual(next(c for c in sync.commands if c[0] == 'add'), ('add', '--', self.note))

    def test_remote_only_pull(self):
        sync = FakeSync(self.root, behind=1)
        commands = self.run_cycle(sync)
        self.assertIn('pull', commands)
        self.assertNotIn('commit', commands)

    def test_preview_never_writes(self):
        sync = FakeSync(self.root, pending=[self.note], behind=1, read_only=True)
        commands = self.run_cycle(sync)
        self.assertTrue({'add', 'commit', 'pull', 'push'}.isdisjoint(commands))

    def test_staged_unrelated_protected_and_deletion_block(self):
        for kwargs in ({'staged': [self.note]}, {'pending': ['other.txt']},
                       {'pending': [module.VAULT + 'Raw/Export/data.json']},
                       {'pending': [module.VAULT + 'missing.md']}):
            with self.subTest(kwargs=kwargs):
                sync = FakeSync(self.root, **kwargs)
                commands = self.run_cycle(sync)
                self.assertEqual(sync.state['status'], 'Needs attention')
                self.assertTrue({'add', 'commit', 'pull', 'push'}.isdisjoint(commands))

    def test_conflict_aborts_and_does_not_push(self):
        sync = FakeSync(self.root, behind=1)
        sync.conflict = True
        commands = self.run_cycle(sync)
        self.assertIn(('rebase', '--abort'), sync.commands)
        self.assertNotIn('push', commands)
        self.assertIn('local commits retained', sync.state['error'])

    def test_unrelated_outgoing_commits_block_push(self):
        sync = FakeSync(self.root)
        sync.outgoing = 'private-outside-vault.txt'
        self.assertNotIn('push', self.run_cycle(sync))
        self.assertEqual(sync.state['status'], 'Needs attention')

    def test_changing_note_waits(self):
        sync = FakeSync(self.root, pending=[self.note])
        with patch.object(module.time, 'sleep', side_effect=lambda _: (self.root / self.note).write_text('still writing')):
            sync.cycle()
        self.assertEqual(sync.state['status'], 'Waiting for edits to settle')
        self.assertNotIn('commit', [c[0] for c in sync.commands])


if __name__ == '__main__': unittest.main()
