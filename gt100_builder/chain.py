"""Access to the stored effect-chain parameters."""

from __future__ import annotations

from typing import Any


def chain_positions(params: dict[str, Any]) -> list[int]:
    """Return the chain ordering, accepting both known storage layouts."""
    nested = params.get("chainParams")
    if isinstance(nested, dict) and isinstance(nested.get("positionList"), list):
        return list(nested["positionList"])
    return [params[f"fx_chain_position{index}"] for index in range(1, 21)]
