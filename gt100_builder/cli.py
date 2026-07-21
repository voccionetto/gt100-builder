"""Dependency-free command-line interface."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .analyzer import ParameterAnalyzer
from .discovery import LibraryAnalysis
from .library import BossLibrary
from .packs import AmbientPack, BassPack, MetalPack, RockPack
from .parser import TSLParser

DEFAULT_SOURCE = Path("templates/LiveSet.tsl")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read and edit Boss GT-100 .TSL files.")
    parser.add_argument("--file", type=Path, default=DEFAULT_SOURCE, help="input .TSL file")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("inspect", help="show LiveSet metadata")
    commands.add_parser("list", help="list patches")
    dump = commands.add_parser("dump", help="print a patch as JSON")
    dump.add_argument("index", type=int)
    rename = commands.add_parser("rename", help="rename a patch")
    rename.add_argument("index", type=int)
    rename.add_argument("name")
    save = commands.add_parser("save", help="save the input LiveSet")
    save.add_argument("output", type=Path)
    groups = commands.add_parser("groups", help="show parameter group counts")
    groups.add_argument("index", type=int, nargs="?", default=0)
    search = commands.add_parser("search", help="search the canonical reference library")
    search.add_argument("query")
    show = commands.add_parser("show", help="show a named canonical preset")
    show.add_argument("name")
    extract = commands.add_parser("extract", help="generate documentation and enum data")
    extract.add_argument("source", type=Path)
    extract.add_argument("--docs", type=Path, default=Path("docs/BossLibrary.md"))
    extract.add_argument("--enums", type=Path, default=Path("gt100_builder/enums.py"))
    enum = commands.add_parser("enums", help="list discovered enum parameters")
    enum.add_argument("source", type=Path)
    diff = commands.add_parser("diff", help="diff two LiveSet files")
    diff.add_argument("before", type=Path)
    diff.add_argument("after", type=Path)
    generate = commands.add_parser("generate", help="generate a reference-derived preset pack")
    generate.add_argument("pack", choices=("bass", "rock", "metal", "ambient"))
    generate.add_argument("source", type=Path)
    generate.add_argument("output", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    args = _parser().parse_args(argv)
    live = TSLParser(args.file).load()
    if args.command == "inspect":
        print(f"Device: {live.device}")
        print(f"Version: {live.version}")
        print(f"Patches: {len(live.patches)}")
        print(f"LiveSet: {live.metadata.get('name', '')}")
    elif args.command == "list":
        for index, patch in enumerate(live.patches):
            print(f"{index:>3}  {patch.name}  [{patch.category or 'Uncategorized'}]")
    elif args.command == "dump":
        print(json.dumps(live.patches[args.index].raw, ensure_ascii=False, indent=2))
    elif args.command == "rename":
        live.patches[args.index].name = args.name
        print(f"Renamed patch {args.index} to {args.name!r}. Use save to write a file.")
    elif args.command == "save":
        live.save(args.output)
        print(f"Saved {args.output}")
    elif args.command == "groups":
        for name, count in ParameterAnalyzer(live.patches[args.index].params).prefixes().most_common():
            print(f"{name:20} {count}")
    elif args.command == "search":
        for patch in BossLibrary.load().search(args.query):
            print(f"{patch.name}  [{patch.category or 'Uncategorized'}]")
    elif args.command == "show":
        print(json.dumps(BossLibrary.load()[args.name].raw, ensure_ascii=False, indent=2))
    elif args.command == "extract":
        analysis = LibraryAnalysis.from_file(args.source)
        args.docs.parent.mkdir(parents=True, exist_ok=True)
        analysis.write_markdown(args.docs, args.source)
        analysis.write_enums(args.enums)
        print(f"Extracted {analysis.patch_count} patches to {args.docs} and {args.enums}")
    elif args.command == "enums":
        for parameter, values in LibraryAnalysis.from_file(args.source).enum_candidates().items():
            print(f"{parameter}: {', '.join(map(str, values))}")
    elif args.command == "diff":
        print(json.dumps(TSLParser(args.before).load().diff(TSLParser(args.after).load()), indent=2))
    elif args.command == "generate":
        library = BossLibrary.load(args.source)
        pack_types = {"bass": BassPack, "rock": RockPack, "metal": MetalPack, "ambient": AmbientPack}
        pack = pack_types[args.pack](library)
        generated = pack.build() if hasattr(pack, "build") else LiveSet()
        generated.save(args.output)
        print(f"Saved {args.pack} pack to {args.output}")

if __name__ == "__main__":
    main()