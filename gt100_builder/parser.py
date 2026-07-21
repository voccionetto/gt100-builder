"""Reader for JSON-based Boss GT-100 ``.TSL`` files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import LiveSet, Patch
from .utils import detect_indent


class TSLParser:
    def __init__(self, filename: str | Path):
        self.filename = Path(filename)

    def load(self) -> LiveSet:
        text = self.filename.read_text(encoding="utf-8")
        data: dict[str, Any] = json.loads(text)
        patches = [
            Patch(
                name=item.get("name", ""),
                gt100_name1=item.get("gt100Name1", ""),
                gt100_name2=item.get("gt100Name2", ""),
                category=item.get("category"),
                params=item.setdefault("params", {}),
                raw=item,
            )
            for item in data.get("patchList", [])
        ]
        return LiveSet(
            version=data.get("version", ""),
            device=data.get("device", "GT"),
            patches=patches,
            metadata=data.setdefault("liveSetData", {}),
            raw=data,
            indent=detect_indent(text),
        )
