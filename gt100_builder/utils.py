"""Small shared helpers."""

from __future__ import annotations

import re


def detect_indent(text: str) -> int | None:
    """Return the indentation width used by JSON, or ``None`` for compact JSON."""
    match = re.search(r"\n( +)\"", text)
    return len(match.group(1)) if match else None
