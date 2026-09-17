"""Conservative categories used by the local rule-based extractor."""
from __future__ import annotations

import re

CATEGORY_FILES = {
    "about_me": "01 - About Me.md",
    "preference": "02 - Preferences.md",
    "education": "03 - Education.md",
    "technical_context": "04 - Programming & Tech.md",
    "project": "05 - Projects.md",
    "career": "06 - Career.md",
    "environment": "07 - Development Environment.md",
    "workflow": "08 - Important Context.md",
    "important_decision": "08 - Important Context.md",
    "recurring_task": "08 - Important Context.md",
}

TECHNOLOGIES = ("Python", "JavaScript", "TypeScript", "React", "Vue", "Angular", "Vite", "Node.js", "Django", "Flask", "FastAPI", "Java", "C#", "C++", "Rust", "Go", "Docker", "Git", "Linux", "Windows", "macOS", "Obsidian", "VS Code", "PostgreSQL", "MySQL", "MongoDB", "AWS", "Azure")


def category_for(statement: str) -> str:
    value = statement.lower()
    if re.search(r"\b(study|studying|student|university|college|degree|course)\b", value):
        return "education"
    if re.search(r"\b(work as|career|portfolio|employed|job|internship|freelance)\b", value):
        return "career"
    if re.search(r"\b(building|developing|my project|project called|project named|creating an app)\b", value):
        return "project"
    if re.search(r"\b(windows|linux|macos|machine|laptop|editor|terminal|environment|setup)\b", value):
        return "environment"
    if re.search(r"\b(prefer|preference|like to|don't like|do not like|always want)\b", value):
        return "preference"
    if re.search(r"\b(decided|decision|must not|never|constraint)\b", value):
        return "important_decision"
    if re.search(r"\b(workflow|usually|every time|routine|recurring)\b", value):
        return "workflow"
    if re.search(r"\b(i am|i'm|my name|i live)\b", value):
        return "about_me"
    return "technical_context"


def technologies_in(statement: str) -> list[str]:
    return [tech for tech in TECHNOLOGIES if re.search(rf"(?<!\w){re.escape(tech)}(?!\w)", statement, re.IGNORECASE)]
