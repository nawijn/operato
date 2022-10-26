#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SENSOR/SENS                /SENSOR/TIME                /SENSOR/VEL                 
# /SENSOR/WORK                /SET                        /SH3N                       
# /SHELL                      /SHEL16                     /SKEW/FIX                   
#

# --- /SENSOR/SENS ------------------------------------------------------
@dataclass
class SensorSens(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/SENS` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/SENS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/TIME ------------------------------------------------------
@dataclass
class SensorTime(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/TIME` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/TIME"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/VEL ------------------------------------------------------
@dataclass
class SensorVel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/VEL` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/VEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/WORK ------------------------------------------------------
@dataclass
class SensorWork(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/WORK` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/WORK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SET ------------------------------------------------------
@dataclass
class Set(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SET` is not implemented.")

    @property
    def keyword(self):
        return "/SET"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SH3N ------------------------------------------------------
@dataclass
class Sh3n(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SH3N` is not implemented.")

    @property
    def keyword(self):
        return "/SH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SHELL ------------------------------------------------------
@dataclass
class Shell(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SHELL` is not implemented.")

    @property
    def keyword(self):
        return "/SHELL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SHEL16 ------------------------------------------------------
@dataclass
class Shel16(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SHEL16` is not implemented.")

    @property
    def keyword(self):
        return "/SHEL16"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SKEW/FIX ------------------------------------------------------
@dataclass
class SkewFix(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SKEW/FIX` is not implemented.")

    @property
    def keyword(self):
        return "/SKEW/FIX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
