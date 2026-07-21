"""Preset collections assembled by cloning reference-library patches."""

from __future__ import annotations

from .library import BossLibrary
from .models import LiveSet, Patch


class _Pack:
    def __init__(self, library: BossLibrary):
        self.library = library

    def _named(self, name: str, fallback: str = "NATURAL CLEAN") -> Patch:
        patch = self.library.get(name) or self.library.get(fallback)
        if patch is None:
            patch = next(iter(self.library))
        return patch

    def build(self) -> LiveSet:
        return LiveSet(metadata={"name": self.__class__.__name__})


class BassPack(_Pack):
    preset_names = [
        "Clean Studio", "Vintage Jazz", "Modern Finger", "Modern Pick", "Marcus Slap", "MusicMan", "Ampeg Style", "GK Style", "Aguilar Style", "Markbass Style", "Darkglass Style", "SansAmp Style", "RHCP", "Rush", "Tool", "Dream Theater", "Jamiroquai", "Gospel Clean", "Worship Ambient", "Chorus Bass", "Octaver", "Synth Bass", "Fretless", "Solo", "Rock Drive",
    ]

    def build(self) -> LiveSet:
        live = super().build()
        for index, name in enumerate(self.preset_names, 1):
            patch = self._named(name, "METAL GtwithBASS" if name in {"Tool", "Rock Drive"} else "NATURAL CLEAN")
            patch.name = f"{index:02} {name}"
            live.add(patch, copy=False)
        return live

    def clean(self) -> Patch:
        return self._named("NATURAL CLEAN")

    def darkglass(self) -> Patch:
        return self._named("METAL GtwithBASS")


class RockPack(_Pack):
    def marshall(self) -> Patch:
        return self._named("BG LEAD", "Hi GAIN STACK")


class AmbientPack(_Pack):
    def worship(self) -> Patch:
        return self._named("NATURAL CLEAN")


class MetalPack(_Pack):
    def build(self) -> LiveSet:
        live = super().build()
        for patch in self.library.search("metal"):
            live.add(patch, copy=False)
        return live


ClassicRockPack = ProgressivePack = FusionPack = GospelPack = RockPack
