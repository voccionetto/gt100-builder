from gt100_builder.parser import TSLParser


def main():
    live = TSLParser("templates/LiveSet.tsl").load()

    print(f"Device : {live.device}")
    print(f"Version: {live.version}")
    print(f"Patches: {len(live.patches)}")

    patch = live.patches[0]

    print()
    print(f"Patch Name : {patch.name}")
    print(f"GT100 Name : {patch.gt100_name1}{patch.gt100_name2}")
    print(f"Category   : {patch.category}")
    print(f"Parameters : {len(patch.params)}")


if __name__ == "__main__":
    main()