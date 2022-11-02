#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ANIM/GPS1                  /ANIM/GPS2                  /ANIM/GZIP                  
# /ANIM/LSENSOR               /ANIM/MASS                  /ANIM/MAT                   
# /ANIM/NODA                  /ANIM/SENSOR                /ANIM/SHELL/DAMA            
#

# --- /ANIM/GPS1 ------------------------------------------------------
@dataclass
class AnimGps1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/GPS1` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/GPS1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/GPS2 ------------------------------------------------------
@dataclass
class AnimGps2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/GPS2` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/GPS2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/GZIP ------------------------------------------------------
@dataclass
class AnimGzip(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/GZIP` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/GZIP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/LSENSOR ------------------------------------------------------
@dataclass
class AnimLsensor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/LSENSOR` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/LSENSOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/MASS ------------------------------------------------------
@dataclass
class AnimMass(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/MASS` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/MASS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/MAT ------------------------------------------------------
@dataclass
class AnimMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/NODA ------------------------------------------------------
@dataclass
class AnimNoda(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/NODA` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/NODA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SENSOR ------------------------------------------------------
@dataclass
class AnimSensor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SENSOR` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SENSOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/DAMA ------------------------------------------------------
@dataclass
class AnimShellDama(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/DAMA` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/DAMA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
