"""Bright, compressed slap starting point."""

from gt100_builder import PatchBuilder


def build():
    return PatchBuilder("NATURAL CLEAN").name("Marcus Slap").preamp(gain=35, bass=60, middle=42, treble=65).compressor(sustain=35, attack=45, level=58).eq(low_gain=3, mid_gain=-2, high_gain=4).build()
