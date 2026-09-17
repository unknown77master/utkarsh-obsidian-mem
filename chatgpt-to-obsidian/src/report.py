"""Human-readable migration and review reports."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .deduplicator import contradiction_candidates
from .obsidian import _write


def write_reports(output: Path, stats: dict[str, Any], memories: list[dict[str, Any]], errors: list[str]) -> list[Path]:
    lines = ["# Migration report", "", "## Source files found", ""]
    lines.extend(f"- {name}" for name in stats.get("source_files", []))
    lines += ["", "## Results", "", f"- Conversations discovered: {stats['discovered']}", f"- Conversations successfully processed: {stats['processed']}", f"- Conversations skipped: {stats['skipped']}", f"- Searchable transcripts: {stats.get('transcripts', 0)}", f"- Raw mirror files: {stats.get('raw_files', 0)}", f"- Raw mirror bytes: {stats.get('raw_bytes', 0)}", f"- Raw files copied: {stats.get('raw_copied', 0)}", f"- Raw files checksum-verified and skipped: {stats.get('raw_skipped', 0)}", f"- Stale raw files removed: {stats.get('raw_removed', 0)}", f"- Local coding projects catalogued: {stats.get('local_projects', 0)}", f"- Public GitHub repositories catalogued: {stats.get('github_projects', 0)}", f"- Errors: {len(errors)}", f"- Memories extracted: {len(memories)}", f"- Duplicates merged: {stats['duplicates']}", f"- Project references detected: {sum(memory['category'] == 'project' for memory in memories)}", f"- Project indexes generated: {stats.get('project_indexes', 0)}", f"- Categories generated: {len({memory['category'] for memory in memories})}", f"- Output files created: {stats.get('output_files', 0)}", "", "## Errors", ""]
    lines.extend(f"- {error}" for error in errors) if errors else lines.append("- None")
    report_path = output / "migration_report.md"
    _write(report_path, "\n".join(lines) + "\n")
    review = ["# Review queue", ""]
    flags = contradiction_candidates(memories)
    if flags:
        for older, newer in flags:
            review += ["## Possible contradiction", "", f"Older/current candidate: {older['statement']}", "", f"Other candidate: {newer['statement']}", "", "Reason: both explicit platform statements may conflict; confirm the current one before treating either as canonical.", ""]
    else:
        review.append("No uncertain contradictions were detected by the conservative local rules.")
    queue_path = output / "review_queue.md"
    _write(queue_path, "\n".join(review) + "\n")
    return [report_path, queue_path]
