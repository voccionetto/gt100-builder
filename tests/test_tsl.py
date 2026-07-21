import json
import tempfile
import unittest
from pathlib import Path

from gt100_builder.parser import TSLParser
from gt100_builder.library import BossLibrary
from gt100_builder.models import LiveSet
from gt100_builder.enums import PreampType
from gt100_builder.enums import CompType
from gt100_builder import PatchBuilder


FIXTURE = Path(__file__).parents[1] / "templates" / "LiveSet.tsl"


class TSLTests(unittest.TestCase):
    def test_parser_loads_patch_and_parameters(self) -> None:
        live = TSLParser(FIXTURE).load()
        self.assertEqual(live.device, "GT")
        self.assertEqual(live.patches[0].name, "Hi GAIN STACK")
        self.assertEqual(live.patches[0].params["preamp_a_gain"], 28)

    def test_writer_round_trip_preserves_data(self) -> None:
        source = json.loads(FIXTURE.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "round-trip.tsl"
            TSLParser(FIXTURE).load().save(output)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), source)

    def test_parameter_api_updates_only_target_value(self) -> None:
        live = TSLParser(FIXTURE).load()
        patch = live.patches[0]
        unknown = patch.params["fx1_sitar_sim_sens"]
        patch.preamp.a.gain = 65
        patch.delay.time = 420
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "edited.tsl"
            live.save(output)
            result = TSLParser(output).load().patches[0]
            self.assertEqual(result.params["preamp_a_gain"], 65)
            self.assertEqual(result.params["delay_delay_time"], 420)
            self.assertEqual(result.params["fx1_sitar_sim_sens"], unknown)

    def test_library_returns_independent_patches(self) -> None:
        library = BossLibrary(TSLParser(FIXTURE).load())
        first = library["Hi GAIN STACK"]
        first.name = "Changed"
        self.assertEqual(library["Hi GAIN STACK"].name, "Hi GAIN STACK")
        self.assertEqual(len(library.search("gain")), 1)

    def test_liveset_add_and_diff(self) -> None:
        patch = TSLParser(FIXTURE).load().patches[0]
        live = LiveSet()
        added = live.add(patch)
        added.preamp.a.gain = 70
        self.assertEqual(patch.preamp.a.gain.value if hasattr(patch.preamp.a.gain, "value") else patch.preamp.a.gain, 28)
        difference = patch.diff(added)
        self.assertEqual(difference["params"]["preamp_a_gain"], {"before": 28, "after": 70})

    def test_selector_parameters_are_enum_aware(self) -> None:
        patch = TSLParser(FIXTURE).load().patches[0]
        self.assertIsInstance(patch.preamp.a.type, PreampType)
        patch.preamp.a.type = "VALUE_4"
        self.assertEqual(patch.params["preamp_a_type"], 4)
        patch.preamp.a.type = 0
        self.assertEqual(patch.preamp.a.type, PreampType.VALUE_0)

    def test_patch_builder_applies_high_level_settings(self) -> None:
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
        self.assertEqual(patch.name, "Studio DI")
        self.assertEqual(patch.params["preamp_a_gain"], 38)
        self.assertEqual(patch.params["comp_type"], 2)
        self.assertEqual(patch.params["eq_low_gain"], 23)
        self.assertEqual(patch.params["delay_on_off"], 0)
        self.assertEqual(patch.params["chorus_on_off"], 0)

    def test_patch_apply_uses_dotted_paths(self) -> None:
        patch = TSLParser(FIXTURE).load().patches[0].clone()
        patch.apply({"preamp.a.gain": 51, "eq.low_gain": 4, "compressor.attack": 42})
        self.assertEqual(patch.params["preamp_a_gain"], 51)
        self.assertEqual(patch.params["eq_low_gain"], 24)
        self.assertEqual(patch.params["comp_attack"], 42)
