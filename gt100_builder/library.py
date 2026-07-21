"""Searchable, read-only access to a canonical Boss preset library."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterator

from .models import LiveSet, Patch
from .parser import TSLParser


class BossLibrary:
    def __init__(self, live_set: LiveSet):
        self._live_set = live_set
        self._by_name = {patch.name.casefold(): patch for patch in live_set.patches}

    @classmethod
    def load(cls, filename: str | Path | None = None) -> "BossLibrary":
        """Load a reference library from a path or the standard local location."""
        path = Path(filename) if filename else cls.default_path()
        return cls(TSLParser(path).load())

    @staticmethod
    def default_path() -> Path:
        configured = os.environ.get("GT100_LIBRARY")
        candidates = [
            Path(configured) if configured else Path("templates/GT-100.tsl"),
            Path("GT-100.tsl"),
        ]
        for candidate in candidates:
            if candidate.exists():
                return candidate
        raise FileNotFoundError("Set GT100_LIBRARY or provide the canonical GT-100.tsl path.")

    def list(self) -> list[str]:
        return [patch.name for patch in self._live_set.patches]

    def search(self, query: str) -> list[Patch]:
        needle = query.casefold()
        return [
            patch.clone()
            for patch in self._live_set.patches
            if needle in patch.name.casefold() or needle in (patch.category or "").casefold()
        ]

    def get(self, name: str) -> Patch | None:
        patch = self._by_name.get(name.casefold())
        return patch.clone() if patch else None

    def __getitem__(self, name: str) -> Patch:
        patch = self.get(name)
        if patch is None:
            raise KeyError(name)
        return patch

    def __iter__(self) -> Iterator[Patch]:
        for patch in self._live_set.patches:
            yield patch.clone()
