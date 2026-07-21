"""Domain models for Boss GT-100 Tone Studio LiveSets."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from copy import deepcopy
from typing import Any

from .parameters import ParameterGroup


@dataclass
class Patch:
    """A patch backed by its original Tone Studio JSON object.

    ``raw`` intentionally holds every field supplied by Tone Studio.  This is
    what lets a caller edit known values without discarding future/unknown ones.
    """

    name: str
    gt100_name1: str = ""
    gt100_name2: str = ""
    category: str | None = None
    params: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.raw:
            self.raw = {"name": self.name, "params": self.params}
        self.raw["params"] = self.params

    def _get_group(self, prefix: str) -> ParameterGroup:
        return ParameterGroup(self.params, prefix)

    @property
    def preamp(self) -> ParameterGroup:
        return self._get_group("preamp")

    @property
    def delay(self) -> ParameterGroup:
        return self._get_group("delay")

    @property
    def eq(self) -> ParameterGroup:
        return self._get_group("eq")

    @property
    def comp(self) -> ParameterGroup:
        return self._get_group("comp")

    @property
    def reverb(self) -> ParameterGroup:
        return self._get_group("reverb")

    @property
    def fx1(self) -> ParameterGroup:
        return self._get_group("fx1")

    @property
    def fx2(self) -> ParameterGroup:
        return self._get_group("fx2")

    def sync(self) -> None:
        """Synchronize convenience fields into the original JSON object."""
        self.raw["name"] = self.name
        self.raw["gt100Name1"] = self.gt100_name1
        self.raw["gt100Name2"] = self.gt100_name2
        self.raw["category"] = self.category
        self.raw["params"] = self.params

    def clone(self) -> "Patch":
        """Return an independent copy suitable for use in another LiveSet."""
        clone = deepcopy(self)
        clone.raw["params"] = clone.params
        return clone

    def apply(self, values: dict[str, Any]) -> "Patch":
        """Apply dotted high-level settings (for example ``preamp.a.gain``)."""
        from .builder import apply_parameters

        return apply_parameters(self, values)

    def diff(self, other: "Patch") -> dict[str, Any]:
        """Describe metadata and parameter differences from another patch."""
        return _mapping_diff(self.raw, other.raw, ignored={"params"}) | {
            "params": _mapping_diff(self.params, other.params)
        }


@dataclass
class LiveSet:
    version: str = "1.0.0"
    device: str = "GT"
    patches: list[Patch] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict, repr=False)
    indent: int | None = field(default=None, repr=False)

    def __post_init__(self) -> None:
        if not self.raw:
            self.raw = {
                "patchList": [patch.raw for patch in self.patches],
                "version": self.version,
                "liveSetData": self.metadata,
                "device": self.device,
            }

    def save(self, filename: str | Path) -> None:
        """Write a Tone Studio compatible ``.TSL`` file."""
        from .writer import TSLWriter

        TSLWriter().write(self, filename)

    def add(self, patch: Patch, *, copy: bool = True) -> Patch:
        """Add a patch, cloning it by default to avoid accidental mutation."""
        item = patch.clone() if copy else patch
        self.patches.append(item)
        self.raw["patchList"] = [current.raw for current in self.patches]
        return item

    def diff(self, other: "LiveSet") -> dict[str, Any]:
        """Compare LiveSets by patch position and top-level metadata."""
        patches: list[dict[str, Any]] = []
        for index in range(max(len(self.patches), len(other.patches))):
            if index >= len(self.patches):
                patches.append({"index": index, "status": "added", "name": other.patches[index].name})
            elif index >= len(other.patches):
                patches.append({"index": index, "status": "removed", "name": self.patches[index].name})
            else:
                changes = self.patches[index].diff(other.patches[index])
                if any(changes.values()):
                    patches.append({"index": index, "status": "changed", "changes": changes})
        return {"metadata": _mapping_diff(self.metadata, other.metadata), "patches": patches}


def _mapping_diff(
    before: dict[str, Any], after: dict[str, Any], ignored: set[str] | None = None
) -> dict[str, dict[str, Any]]:
    ignored = ignored or set()
    keys = set(before) | set(after)
    return {
        key: {"before": before.get(key), "after": after.get(key)}
        for key in sorted(keys - ignored)
        if before.get(key) != after.get(key)
    }
