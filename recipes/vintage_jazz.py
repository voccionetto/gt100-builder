"""Warm, rounded clean variation."""

from gt100_builder import PatchBuilder


def build():
    return PatchBuilder("NATURAL CLEAN").name("Vintage Jazz").preamp(gain=32, bass=58, middle=55, treble=45).eq(low_gain=2, mid_gain=1, high_gain=-2).disable("delay").build()
