#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SENSOR/DIST_SURF           /SENSOR/ENERGY              /SENSOR/GAUGE               
# /SENSOR/HIC                 /SENSOR/INTER               /SENSOR/NOT                 
# /SENSOR/RBODY               /SENSOR/RWALL               /SENSOR/SECT                
#

# --- /SENSOR/DIST_SURF ------------------------------------------------------
@dataclass
class SensorDistSurf(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/DIST_SURF` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/DIST_SURF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/ENERGY ------------------------------------------------------
@dataclass
class SensorEnergy(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/ENERGY` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/ENERGY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/GAUGE ------------------------------------------------------
@dataclass
class SensorGauge(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/GAUGE` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/GAUGE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/HIC ------------------------------------------------------
@dataclass
class SensorHic(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/HIC` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/HIC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/INTER ------------------------------------------------------
@dataclass
class SensorInter(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/INTER` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/INTER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/NOT ------------------------------------------------------
@dataclass
class SensorNot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/NOT` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/NOT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/RBODY ------------------------------------------------------
@dataclass
class SensorRbody(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/RBODY` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/RBODY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/RWALL ------------------------------------------------------
@dataclass
class SensorRwall(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/RWALL` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/RWALL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/SECT ------------------------------------------------------
@dataclass
class SensorSect(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/SECT` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/SECT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
