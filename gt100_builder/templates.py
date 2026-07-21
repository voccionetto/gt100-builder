"""Reusable, conservative patch templates."""

from __future__ import annotations

from .models import Patch


class _Template:
    category: str | None = None

    @classmethod
    def apply(cls, patch: Patch) -> Patch:
        if cls.category:
            patch.category = cls.category
        return patch


class CleanTemplate(_Template):
    category = "STUDIO"


class CrunchTemplate(_Template):
    category = "ROCK"


class LeadTemplate(_Template):
    category = "ROCK"


class BassTemplate(_Template):
    category = "STUDIO"


class MetalTemplate(_Template):
    category = "METAL"


class AmbientTemplate(_Template):
    category = "STUDIO"
