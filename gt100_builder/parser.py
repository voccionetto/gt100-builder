import json
from pathlib import Path

from gt100_builder.models import LiveSet, Patch


class TSLParser:
    def __init__(self, filename: str | Path):
        self.filename = Path(filename)

    def load(self) -> LiveSet:
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        patches = []

        for p in data["patchList"]:
            patches.append(
                Patch(
                    name=p["name"],
                    gt100_name1=p["gt100Name1"],
                    gt100_name2=p["gt100Name2"],
                    category=p.get("category"),
                    params=p["params"],
                    raw=p,
                )
            )

        return LiveSet(
            version=data["version"],
            device=data["device"],
            patches=patches,
            metadata=data["liveSetData"],
        )