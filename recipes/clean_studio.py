"""Neutral bass-oriented clean foundation."""

from gt100_builder import PatchBuilder
from gt100_builder.enums import CompType, PreampType


def build():
    return (
        PatchBuilder("NATURAL CLEAN")
        .name("Clean Studio")
        .preamp(type=PreampType.NATURAL_CLEAN, gain=38, bass=55, middle=48, treble=58, level=70)
        .compressor(type=CompType.BASS_COMP, sustain=30, attack=40, level=55)
        .eq(low_gain=3, mid_gain=2, high_gain=1)
        .disable("delay")
        .disable("chorus")
        .build()
    )
