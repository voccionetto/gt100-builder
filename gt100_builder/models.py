from dataclasses import dataclass
from typing import Any


@dataclass
class Patch:
    name: str
    gt100_name1: str
    gt100_name2: str
    category: str | None
    params: dict[str, Any]
    raw: dict[str, Any]


@dataclass
class LiveSet:
    version: str
    device: str
    patches: list[Patch]
    metadata: dict[str, Any]