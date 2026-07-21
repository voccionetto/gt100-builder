"""Writer that preserves the complete original Tone Studio structure."""

from __future__ import annotations

import json
from pathlib import Path

from .models import LiveSet


class TSLWriter:
    def write(self, live_set: LiveSet, filename: str | Path) -> None:
        for patch in live_set.patches:
            patch.sync()
        live_set.raw["patchList"] = [patch.raw for patch in live_set.patches]
        live_set.raw["version"] = live_set.version
        live_set.raw["device"] = live_set.device
        live_set.raw["liveSetData"] = live_set.metadata
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        if live_set.indent is None:
            content = json.dumps(live_set.raw, ensure_ascii=False, separators=(",", ":"))
        else:
            content = json.dumps(live_set.raw, ensure_ascii=False, indent=live_set.indent)
        path.write_text(content, encoding="utf-8")
