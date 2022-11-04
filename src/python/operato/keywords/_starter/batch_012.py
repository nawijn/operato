#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /FAIL/MULLINS_OR            /FAIL/NXT                   /FAIL/ORTHBIQUAD            
# /FAIL/ORTHSTRAIN            /FAIL/PUCK                  /FAIL/RTCL                  
# /FAIL/SAHRAEI               /FAIL/SNCONNECT             /FAIL/SPALLING              
#

# --- /FAIL/MULLINS_OR ------------------------------------------------------
@dataclass
class FailMullinsOr(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/MULLINS_OR` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/MULLINS_OR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/NXT ------------------------------------------------------
@dataclass
class FailNxt(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/NXT` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/NXT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/ORTHBIQUAD ------------------------------------------------------
@dataclass
class FailOrthbiquad(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/ORTHBIQUAD` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/ORTHBIQUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/ORTHSTRAIN ------------------------------------------------------
@dataclass
class FailOrthstrain(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/ORTHSTRAIN` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/ORTHSTRAIN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/PUCK ------------------------------------------------------
@dataclass
class FailPuck(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/PUCK` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/PUCK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/RTCL ------------------------------------------------------
@dataclass
class FailRtcl(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/RTCL` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/RTCL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/SAHRAEI ------------------------------------------------------
@dataclass
class FailSahraei(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/SAHRAEI` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/SAHRAEI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/SNCONNECT ------------------------------------------------------
@dataclass
class FailSnconnect(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/SNCONNECT` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/SNCONNECT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/SPALLING ------------------------------------------------------
@dataclass
class FailSpalling(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/SPALLING` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/SPALLING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
