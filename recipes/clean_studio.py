"""Studio DI - Ultra Clean"""

from gt100_builder import PatchBuilder
from gt100_builder.enums import CompType, PreampType


def build():
    return (
        PatchBuilder("NATURAL CLEAN")
        .name("Clean Studio")

        .preamp(
            type=PreampType.NATURAL_CLEAN,
            gain=28,
            bass=52,
            middle=50,
            treble=54,
            level=78,
        )

        .compressor(
            type=CompType.BASS_COMP,
            sustain=22,
            attack=18,
            level=60,
        )

        .eq(
            low_gain=2,
            mid_gain=0,
            high_gain=1,
        )

        .disable("chorus")
        .disable("delay")
        .disable("reverb")

        .build()
    )