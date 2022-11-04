#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /TH/SECTIO                  /TH/SH3N                    /TH/SHEL                    
# /TH/SLIPRING                /TH/SPH_FLOW                /TH/SPHCEL                  
# /TH/SPRING                  /TH/SUBS                    /TH/SURF                    
#

# --- /TH/SECTIO ------------------------------------------------------
@dataclass
class ThSectio(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SECTIO` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SECTIO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/SH3N ------------------------------------------------------
@dataclass
class ThSh3n(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SH3N` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/SHEL ------------------------------------------------------
@dataclass
class ThShel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SHEL` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SHEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/SLIPRING ------------------------------------------------------
@dataclass
class ThSlipring(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SLIPRING` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SLIPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/SPH_FLOW ------------------------------------------------------
@dataclass
class ThSphFlow(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SPH_FLOW` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SPH_FLOW"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/SPHCEL ------------------------------------------------------
@dataclass
class ThSphcel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SPHCEL` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SPHCEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/SPRING ------------------------------------------------------
@dataclass
class ThSpring(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SPRING` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/SUBS ------------------------------------------------------
@dataclass
class ThSubs(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SUBS` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SUBS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/SURF ------------------------------------------------------
@dataclass
class ThSurf(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/SURF` is not implemented.")

    @property
    def keyword(self):
        return "/TH/SURF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
