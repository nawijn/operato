#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /TH/ACCEL                   /TH/BEAM                    /TH/BRIC
# /TH/CLUSTER                 /TH/CYL_JO                  /TH/FRAME
# /TH/FXBODY                  /TH/GAUGE                   /TH/INTER
#

# --- /TH/ACCEL ------------------------------------------------------
@dataclass
class ThAccel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/ACCEL` is not implemented.")

    @property
    def keyword(self):
        return "/TH/ACCEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TH/BEAM ------------------------------------------------------
@dataclass
class ThBeam(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/BEAM` is not implemented.")

    @property
    def keyword(self):
        return "/TH/BEAM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TH/BRIC ------------------------------------------------------
@dataclass
class ThBric(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/BRIC` is not implemented.")

    @property
    def keyword(self):
        return "/TH/BRIC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TH/CLUSTER ------------------------------------------------------
@dataclass
class ThCluster(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/CLUSTER` is not implemented.")

    @property
    def keyword(self):
        return "/TH/CLUSTER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TH/CYL_JO ------------------------------------------------------
@dataclass
class ThCylJo(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/CYL_JO` is not implemented.")

    @property
    def keyword(self):
        return "/TH/CYL_JO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TH/FRAME ------------------------------------------------------
@dataclass
class ThFrame(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/FRAME` is not implemented.")

    @property
    def keyword(self):
        return "/TH/FRAME"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TH/FXBODY ------------------------------------------------------
@dataclass
class ThFxbody(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/FXBODY` is not implemented.")

    @property
    def keyword(self):
        return "/TH/FXBODY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TH/GAUGE ------------------------------------------------------
@dataclass
class ThGauge(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/GAUGE` is not implemented.")

    @property
    def keyword(self):
        return "/TH/GAUGE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TH/INTER ------------------------------------------------------
@dataclass
class ThInter(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/INTER` is not implemented.")

    @property
    def keyword(self):
        return "/TH/INTER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
