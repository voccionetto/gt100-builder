# GT100 Builder

`gt100-builder` is a dependency-free Python SDK for Boss GT-100 Tone Studio
(`.TSL`) LiveSets. It retains the source JSON object and all unknown parameters
when saving.

```python
from gt100_builder import TSLParser

live = TSLParser("LiveSet.tsl").load()
patch = live.patches[0]
patch.name = "Rock Solo"
patch.preamp.a.gain = 65
patch.delay.time = 420
patch.eq.low_gain = 23
live.save("edited.tsl")
```

## Patch Builder

Create tones by editing Python recipes, never the raw Tone Studio JSON. A builder
clones a known-good factory patch and changes only the named settings:

```python
from gt100_builder import CompType, PatchBuilder, PreampType

patch = (
    PatchBuilder("NATURAL CLEAN")
    .name("Studio DI")
    .preamp(type=PreampType.NATURAL_CLEAN, gain=38, bass=55, middle=48, treble=58, level=70)
    .compressor(type=CompType.BASS_COMP, sustain=30, attack=40, level=55)
    .eq(low_gain=3, mid_gain=2, high_gain=1)
    .disable("delay")
    .disable("chorus")
    .build()
)
```

Builder blocks include `preamp`, `compressor`, `eq`, `od_ds`, `fx1`, `fx2`,
`delay`, `reverb`, `ns`, and `ctl`. `Patch.apply()` also accepts high-level
dotted paths such as `{"preamp.a.gain": 38, "eq.low_gain": 3}`. EQ gain
values are expressed in dB (`-20` to `20`) and translated to the underlying
Tone Studio representation.

The editable starting recipes are in [recipes](recipes/): `clean_studio`,
`vintage_jazz`, `marcus_slap`, `darkglass`, `aguilar`, and `markbass`.

## Reference library

The factory `GT-100.tsl` is used as a local knowledge base rather than being
hardcoded into the SDK. Generate its documentation and observed numeric enums:

```text
python generate_pack.py extract D:\Downloads\GT-100.tsl
```

Searches and lookups always return deep copies, so factory originals cannot be
modified accidentally:

```python
from gt100_builder import BossLibrary, LiveSet

library = BossLibrary.load("GT-100.tsl")
clean = library["NATURAL CLEAN"]
results = library.search("lead")

live = LiveSet(metadata={"name": "My collection"})
live.add(clean)
live.save("collection.tsl")
```

Use `GT100_LIBRARY` to configure the default reference path for CLI searches.

## Collections and comparison

```python
from gt100_builder import BassPack, BossLibrary

library = BossLibrary.load("GT-100.tsl")
bass_collection = BassPack(library).build()
bass_collection.save("Bass Collection.tsl")

changes = original_patch.diff(edited_patch)
```

Run the command line interface through the included script:

```text
python generate_pack.py inspect
python generate_pack.py list
python generate_pack.py dump 0
python generate_pack.py groups
python generate_pack.py save output/test.tsl
python generate_pack.py search clean
python generate_pack.py show "BG LEAD"
python generate_pack.py enums D:\Downloads\GT-100.tsl
python generate_pack.py diff first.tsl second.tsl
python generate_pack.py generate bass D:\Downloads\GT-100.tsl output/bass.tsl
```

Use `--file path/to/LiveSet.tsl` before the command to select another input file.
