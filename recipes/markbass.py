"""Clear, slightly scooped bass starting point."""

from gt100_builder import PatchBuilder


def build():
    return PatchBuilder("NATURAL CLEAN").name("Markbass Style").preamp(gain=36, bass=56, middle=45, treble=60).eq(low_gain=2, mid_gain=-2, high_gain=2).build()
