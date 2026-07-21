"""Mid-focused bass starting point."""

from gt100_builder import PatchBuilder


def build():
    return PatchBuilder("NATURAL CLEAN").name("Aguilar Style").preamp(gain=40, bass=58, middle=58, treble=52).eq(low_gain=2, mid_gain=4, high_gain=0).build()
