#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, KeywordCategory, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ABF                        /ADYREL                     /ALE/GRID/DISP
# /ALE/GRID/DONEA             /ALE/GRID/SPRING            /ALE/GRID/STANDARD
# /ALE/GRID/ZERO              /ALE/LINK/OFF               /ALE/LINK/ON
#

# --- /ABF ------------------------------------------------------
@dataclass
class Abf(Keyword):
    """Describes the output of .abf files. (.abf [binary] files are optimized
    for fast plotting of very large data sets and is intended for creating 2D
    and 3D plots using HyperGraph and HyperGraph 3D).
    """

    dt_abf: float
    dt_t_w_abv: float

    @property
    def keyword(self):
        return "/ABF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [[FloatField("dt_abf", 1), FloatField("dt_t_w_abv", 3)]]

        return structure


# --- /ADYREL ------------------------------------------------------
@dataclass
class Adyrel(Keyword):
    """Dynamic relaxation with auto-defined adaptive damping."""

    t_start: float = 0.0
    t_stop: float | None = None

    @property
    def keyword(self):
        return "/ADYREL"

    @property
    def pre_conditions(self):
        if self.t_stop is None:
            return []

        return [
            (self.t_stop > self.t_start, "Pre-condition `t_stop > t_start` is violated")
        ]

    @property
    def structure(self):
        structure = [[FloatField("t_start", 1), FloatField("t_stop", 3)]]

        return structure


# --- /ALE/GRID/DISP ------------------------------------------------------
@dataclass
class AleGridDisp(Keyword):
    u_max: float
    v_min: float

    @property
    def keyword(self):
        return "/ALE/GRID/DISP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [[FloatField("u_max", 1), FloatField("v_min", 3)]]

        return structure


# --- /ALE/GRID/DONEA ------------------------------------------------------
@dataclass
class AleGridDonea(Keyword):
    alpha: float
    gamma: float
    fscale_x: float
    fscale_y: float
    fscale_z: float
    v_min: float

    @property
    def keyword(self):
        return "/ALE/GRID/DONEA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        # We need to treat this keyword a little different because it has 6 float fields
        # on a single line. This is not allowed for starter keywords, but it is allowed
        # for engine keywords because the lines are free formatted.
        self.type = KeywordCategory.ENGINE

        structure = [
            [
                FloatField("alpha", 1),
                FloatField("gamma", 3),
                FloatField("fscale_x", 5),
                FloatField("fscale_y", 7),
                FloatField("fscale_z", 9),
                FloatField("v_min", 11),
            ]
        ]

        return structure


# --- /ALE/GRID/SPRING ------------------------------------------------------
@dataclass
class AleGridSpring(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/GRID/SPRING` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/GRID/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ALE/GRID/STANDARD ------------------------------------------------------
@dataclass
class AleGridStandard(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/GRID/STANDARD` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/GRID/STANDARD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ALE/GRID/ZERO ------------------------------------------------------
@dataclass
class AleGridZero(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/GRID/ZERO` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/GRID/ZERO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ALE/LINK/OFF ------------------------------------------------------
@dataclass
class AleLinkOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/LINK/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/LINK/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ALE/LINK/ON ------------------------------------------------------
@dataclass
class AleLinkOn(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/LINK/ON` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/LINK/ON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
