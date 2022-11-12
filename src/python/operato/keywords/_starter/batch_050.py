#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SKEW/MOV                   /SKEW/MOV2                  /SLIPRING/SHELL             
# /SLIPRING/SPRING            /SPH/INOUT                  /SPH/RESERVE                
# /SPHBCS                     /SPHCEL                     /SPHGLO                     
#

# --- /SKEW/MOV ------------------------------------------------------
@dataclass
class SkewMov(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SKEW/MOV` is not implemented.")

    @property
    def keyword(self):
        return "/SKEW/MOV"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SKEW/MOV2 ------------------------------------------------------
@dataclass
class SkewMov2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SKEW/MOV2` is not implemented.")

    @property
    def keyword(self):
        return "/SKEW/MOV2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SLIPRING/SHELL ------------------------------------------------------
@dataclass
class SlipringShell(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SLIPRING/SHELL` is not implemented.")

    @property
    def keyword(self):
        return "/SLIPRING/SHELL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SLIPRING/SPRING ------------------------------------------------------
@dataclass
class SlipringSpring(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SLIPRING/SPRING` is not implemented.")

    @property
    def keyword(self):
        return "/SLIPRING/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SPH/INOUT ------------------------------------------------------
@dataclass
class SphInout(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SPH/INOUT` is not implemented.")

    @property
    def keyword(self):
        return "/SPH/INOUT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SPH/RESERVE ------------------------------------------------------
@dataclass
class SphReserve(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SPH/RESERVE` is not implemented.")

    @property
    def keyword(self):
        return "/SPH/RESERVE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SPHBCS ------------------------------------------------------
@dataclass
class Sphbcs(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SPHBCS` is not implemented.")

    @property
    def keyword(self):
        return "/SPHBCS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SPHCEL ------------------------------------------------------
@dataclass
class Sphcel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SPHCEL` is not implemented.")

    @property
    def keyword(self):
        return "/SPHCEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SPHGLO ------------------------------------------------------
@dataclass
class Sphglo(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SPHGLO` is not implemented.")

    @property
    def keyword(self):
        return "/SPHGLO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
