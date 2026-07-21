"""Lightweight, non-destructive parameter accessors."""

from __future__ import annotations

from typing import Any


def _enum_for(parameter: str) -> type | None:
    try:
        from .enums import PARAMETER_ENUMS

        return PARAMETER_ENUMS.get(parameter)
    except ImportError:
        return None


class ParameterGroup:
    """Expose parameter prefixes through Python attributes.

    Attribute names traverse groups where possible: ``patch.preamp.a.gain``
    maps to ``preamp_a_gain``. Direct dictionary access remains available for
    names that are not valid Python identifiers.
    """

    def __init__(self, params: dict[str, Any], prefix: str):
        object.__setattr__(self, "_params", params)
        object.__setattr__(self, "_prefix", prefix)

    def __getattr__(self, name: str) -> Any:
        key = f"{self._prefix}_{name}"
        if self._prefix == "delay" and name == "time":
            key = "delay_delay_time"
        if key in self._params:
            enum_type = _enum_for(key)
            value = self._params[key]
            if enum_type is not None:
                try:
                    return enum_type(value)
                except ValueError:
                    return value
            return value
        prefix = f"{key}_"
        if any(item.startswith(prefix) for item in self._params):
            return ParameterGroup(self._params, key)
        raise AttributeError(f"Unknown GT-100 parameter: {key}")

    def __setattr__(self, name: str, value: Any) -> None:
        key = f"{self._prefix}_{name}"
        if self._prefix == "delay" and name == "time":
            key = "delay_delay_time"
        enum_type = _enum_for(key)
        if isinstance(value, str) and enum_type is not None:
            normalized = value.strip().upper().replace(" ", "_").replace("-", "_")
            try:
                value = enum_type[normalized]
            except KeyError as error:
                raise ValueError(f"Unknown {enum_type.__name__} member: {value}") from error
        self._params[key] = value.value if hasattr(value, "value") else value

    def get(self, name: str, default: Any = None) -> Any:
        return self._params.get(f"{self._prefix}_{name}", default)

    def set(self, name: str, value: Any) -> None:
        self._params[f"{self._prefix}_{name}"] = value
