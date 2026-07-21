"""Tools that derive SDK knowledge from a canonical GT-100 LiveSet."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .parser import TSLParser


@dataclass
class LibraryAnalysis:
    patch_count: int
    categories: Counter[str]
    parameter_values: dict[str, Counter[Any]]
    parameter_ranges: dict[str, tuple[int | float, int | float]]

    @classmethod
    def from_file(cls, filename: str | Path) -> "LibraryAnalysis":
        live = TSLParser(filename).load()
        values: dict[str, Counter[Any]] = defaultdict(Counter)
        categories: Counter[str] = Counter()
        for patch in live.patches:
            categories[patch.category or "Uncategorized"] += 1
            for name, value in patch.params.items():
                if not isinstance(value, (dict, list)):
                    values[name][value] += 1
        ranges = {
            name: (min(counter), max(counter))
            for name, counter in values.items()
            if counter and all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in counter)
        }
        return cls(len(live.patches), categories, dict(values), ranges)

    def enum_candidates(self) -> dict[str, list[int]]:
        """Find compact integer domains likely to represent selector values."""
        candidates: dict[str, list[int]] = {}
        for name, counter in self.parameter_values.items():
            values = list(counter)
            selector = name.endswith(("_type", "_mode", "_on_off", "_fx_type", "_select", "_sw"))
            if selector and values and len(values) <= 32 and all(isinstance(value, int) for value in values):
                candidates[name] = sorted(values)
        return candidates

    def write_enums(self, target: str | Path) -> None:
        target = Path(target)
        lines = [
            '"""Auto-generated numeric selectors observed in the canonical GT-100 library."""',
            "from enum import IntEnum",
            "",
        ]
        mappings: list[str] = []
        emitted: set[str] = set()
        for parameter, values in self.enum_candidates().items():
            class_name = _class_name(parameter)
            if class_name in emitted:
                mappings.append(f'    "{parameter}": {class_name},')
                continue
            lines.extend([f"class {class_name}(IntEnum):"])
            lines.extend([f"    VALUE_{value} = {value}" for value in values])
            lines.append("")
            mappings.append(f'    "{parameter}": {class_name},')
            emitted.add(class_name)
        lines.extend(["PARAMETER_ENUMS = {", *mappings, "}", ""])
        target.write_text("\n".join(lines), encoding="utf-8")

    def write_markdown(self, filename: str | Path, source: str | Path) -> None:
        live = TSLParser(source).load()
        lines = ["# Boss GT-100 Factory Library", "", f"Analyzed patches: {self.patch_count}", "", "## Categories", ""]
        lines.extend(f"- {name}: {count}" for name, count in self.categories.most_common())
        lines.extend(["", "## Patches", ""])
        for patch in live.patches:
            params = patch.params
            enabled = [name for name in ("comp", "eq", "delay", "chorus", "reverb", "fx1", "fx2", "pedal_fx") if params.get(f"{name}_on_off")]
            lines.extend([
                f"### {patch.name}", "",
                f"- Category: {patch.category or 'Uncategorized'}",
                f"- Enabled effects: {', '.join(enabled) or 'None'}",
                f"- Preamp: A type {params.get('preamp_a_type')}; B type {params.get('preamp_b_type')}",
                f"- Cabinet: A {params.get('preamp_a_sp_type')}; B {params.get('preamp_b_sp_type')}",
                f"- Compressor: {params.get('comp_type')}",
                f"- EQ: {'on' if params.get('eq_on_off') else 'off'}",
                f"- Delay: type {params.get('delay_type')}, {'on' if params.get('delay_on_off') else 'off'}",
                f"- Reverb: type {params.get('reverb_type')}, {'on' if params.get('reverb_on_off') else 'off'}",
                f"- FX1 / FX2: {params.get('fx1_fx_type')} / {params.get('fx2_fx_type')}",
                f"- Pedal FX: {'on' if params.get('pedal_fx_on_off') else 'off'}",
                f"- Active assigns: {sum(params.get(f'assign{i}_on_off', 0) for i in range(1, 9))}",
                f"- Patch level: {params.get('patch_level')}", "",
            ])
        lines.extend(["## Observed Selector Values", ""])
        for parameter, values in self.enum_candidates().items():
            usage = self.parameter_values[parameter]
            detail = ", ".join(f"{value} ({usage[value]})" for value in values)
            lines.append(f"- `{parameter}`: {detail}")
        Path(filename).write_text("\n".join(lines), encoding="utf-8")


def _class_name(parameter: str) -> str:
    if parameter in {"preamp_a_type", "preamp_b_type"}:
        return "PreampType"
    return "".join(part.capitalize() for part in parameter.split("_"))
