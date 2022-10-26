#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /FRAME/MOV2                 /FRAME/NOD                  /FRIC_ORIENT                
# /FRICTION                   /FUNC_2D                    /FUNCT                      
# /FUNCT_SMOOTH               /FXBODY                     /GAUGE                      
#

# --- /FRAME/MOV2 ------------------------------------------------------
@dataclass
class FrameMov2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FRAME/MOV2` is not implemented.")

    @property
    def keyword(self):
        return "/FRAME/MOV2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FRAME/NOD ------------------------------------------------------
@dataclass
class FrameNod(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FRAME/NOD` is not implemented.")

    @property
    def keyword(self):
        return "/FRAME/NOD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FRIC_ORIENT ------------------------------------------------------
@dataclass
class FricOrient(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FRIC_ORIENT` is not implemented.")

    @property
    def keyword(self):
        return "/FRIC_ORIENT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FRICTION ------------------------------------------------------
@dataclass
class Friction(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FRICTION` is not implemented.")

    @property
    def keyword(self):
        return "/FRICTION"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FUNC_2D ------------------------------------------------------
@dataclass
class Func2d(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FUNC_2D` is not implemented.")

    @property
    def keyword(self):
        return "/FUNC_2D"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FUNCT ------------------------------------------------------
@dataclass
class Funct(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FUNCT` is not implemented.")

    @property
    def keyword(self):
        return "/FUNCT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FUNCT_SMOOTH ------------------------------------------------------
@dataclass
class FunctSmooth(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FUNCT_SMOOTH` is not implemented.")

    @property
    def keyword(self):
        return "/FUNCT_SMOOTH"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FXBODY ------------------------------------------------------
@dataclass
class Fxbody(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FXBODY` is not implemented.")

    @property
    def keyword(self):
        return "/FXBODY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GAUGE ------------------------------------------------------
@dataclass
class Gauge(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GAUGE` is not implemented.")

    @property
    def keyword(self):
        return "/GAUGE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
