#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /RWALL/LAGMUL               /RWALL/THERM                /SECT                       
# /SECT/CIRCLE                /SECT/PARAL                 /SENSOR                     
# /SENSOR/ACCE                /SENSOR/AND_OR              /SENSOR/DIST                
#

# --- /RWALL/LAGMUL ------------------------------------------------------
@dataclass
class RwallLagmul(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RWALL/LAGMUL` is not implemented.")

    @property
    def keyword(self):
        return "/RWALL/LAGMUL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RWALL/THERM ------------------------------------------------------
@dataclass
class RwallTherm(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RWALL/THERM` is not implemented.")

    @property
    def keyword(self):
        return "/RWALL/THERM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SECT ------------------------------------------------------
@dataclass
class Sect(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SECT` is not implemented.")

    @property
    def keyword(self):
        return "/SECT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SECT/CIRCLE ------------------------------------------------------
@dataclass
class SectCircle(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SECT/CIRCLE` is not implemented.")

    @property
    def keyword(self):
        return "/SECT/CIRCLE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SECT/PARAL ------------------------------------------------------
@dataclass
class SectParal(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SECT/PARAL` is not implemented.")

    @property
    def keyword(self):
        return "/SECT/PARAL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR ------------------------------------------------------
@dataclass
class Sensor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/ACCE ------------------------------------------------------
@dataclass
class SensorAcce(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/ACCE` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/ACCE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/AND_OR ------------------------------------------------------
@dataclass
class SensorAndOr(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/AND_OR` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/AND_OR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SENSOR/DIST ------------------------------------------------------
@dataclass
class SensorDist(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SENSOR/DIST` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/DIST"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
