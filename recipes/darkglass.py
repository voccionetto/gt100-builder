"""Driven bass starting point based on the factory bass-oriented preset."""

from gt100_builder import PatchBuilder


def build():
    return PatchBuilder("METAL GtwithBASS").name("Darkglass Style").preamp(gain=48, bass=58, middle=52, treble=56).od_ds(drive=55, tone=55, effect_level=50).build()
