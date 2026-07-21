"""High-level, non-destructive construction of GT-100 patches."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

from .library import BossLibrary
from .models import Patch


class PatchBuilder:
    """Build a patch by applying musical settings to a known-good base patch."""

    def __init__(self, base: str | Patch = "NATURAL CLEAN", library: BossLibrary | None = None):
        if isinstance(base, Patch):
            self._patch = base.clone()
        else:
            self._patch = (library or BossLibrary.load())[base]

    def name(self, value: str) -> "PatchBuilder":
        self._patch.name = value
        return self

    def apply(self, values: Mapping[str, Any]) -> "PatchBuilder":
        apply_parameters(self._patch, values)
        return self

    def preamp(self, **values: Any) -> "PatchBuilder":
        return self._block("preamp", values)

    def compressor(self, **values: Any) -> "PatchBuilder":
        return self._block("compressor", values)

    def eq(self, **values: Any) -> "PatchBuilder":
        return self._block("eq", values)

    def od_ds(self, **values: Any) -> "PatchBuilder":
        return self._block("od_ds", values)

    def fx1(self, **values: Any) -> "PatchBuilder":
        return self._block("fx1", values)

    def fx2(self, **values: Any) -> "PatchBuilder":
        return self._block("fx2", values)

    def delay(self, **values: Any) -> "PatchBuilder":
        return self._block("delay", values)

    def reverb(self, **values: Any) -> "PatchBuilder":
        return self._block("reverb", values)

    def ns(self, **values: Any) -> "PatchBuilder":
        return self._block("ns", values)

    def ctl(self, **values: Any) -> "PatchBuilder":
        return self._block("ctl", values)

    def enable(self, block: str) -> "PatchBuilder":
        self._set_enabled(block, True)
        return self

    def disable(self, block: str) -> "PatchBuilder":
        self._set_enabled(block, False)
        return self

    def build(self) -> Patch:
        """Return the normal project ``Patch`` model, not a builder wrapper."""
        return self._patch

    def _block(self, block: str, values: Mapping[str, Any]) -> "PatchBuilder":
        if block != "ctl":
            self._set_enabled(block, True)
        return self.apply({f"{block}.{key}": value for key, value in values.items()})

    def _set_enabled(self, block: str, enabled: bool) -> None:
        key = _enable_key(block)
        self._patch.params[key] = int(enabled)


def apply_parameters(patch: Patch, values: Mapping[str, Any]) -> Patch:
    """Apply dotted, high-level settings to a patch and return it.

    This deliberately changes only referenced parameters; all factory and
    unknown values on the base patch remain intact.
    """
    for path, value in values.items():
        _apply_one(patch, path, value)
    return patch


def _apply_one(patch: Patch, path: str, value: Any) -> None:
    parts = path.split(".")
    if not parts or any(not part for part in parts):
        raise ValueError(f"Invalid parameter path: {path!r}")
    block = parts[0]
    name = "_".join(parts[1:])
    if block == "preamp":
        if len(parts) == 2:
            name = f"a_{parts[1]}"
        raw_name = f"preamp_{name}"
    elif block == "compressor":
        raw_name = f"comp_{name}"
    elif block == "eq":
        raw_name = _eq_name(name)
        value = _encode_eq(value) if raw_name.endswith("_gain") else value
    elif block == "delay":
        raw_name = {"time": "delay_delay_time", "feedback": "delay_f_back"}.get(name, f"delay_{name}")
    elif block == "ns":
        raw_name = f"ns1_{name}"
    elif block in {"od_ds", "fx1", "fx2", "reverb", "ctl"}:
        raw_name = f"{block}_{name}"
        if block in {"fx1", "fx2"} and name == "type":
            raw_name = f"{block}_fx_type"
    else:
        raise ValueError(f"Unsupported high-level block: {block!r}")
    if raw_name not in patch.params:
        raise AttributeError(f"{path!r} is not available on this GT-100 patch")
    patch.params[raw_name] = value.value if hasattr(value, "value") else value


def _enable_key(block: str) -> str:
    aliases = {"compressor": "comp", "ns": "ns1", "preamp": "preamp_a"}
    prefix = aliases.get(block, block)
    key = f"{prefix}_on_off"
    if block == "od_ds":
        key = "od_ds_on_off"
    return key


def _eq_name(name: str) -> str:
    aliases = {
        "mid_gain": "eq_low_mid_gain",
        "high_gain": "eq_high_gain",
        "low_gain": "eq_low_gain",
    }
    return aliases.get(name, f"eq_{name}")


def _encode_eq(value: Any) -> Any:
    """Convert user-facing dB gain (-20..20) to Tone Studio's 0..40 value."""
    if isinstance(value, (int, float)) and -20 <= value <= 20:
        return value + 20
    return value
