#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SURF/SEG                   /SURF/SUBMODEL              /SURF/SUBSET                
# /SURF/SURF                  /TABLE/0                    /TABLE/1                    
# /TETRA4                     /TETRA10                    /TH                         
#

# --- /SURF/SEG ------------------------------------------------------
@dataclass
class SurfSeg(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/SEG` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/SEG"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/SUBMODEL ------------------------------------------------------
@dataclass
class SurfSubmodel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/SUBMODEL` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/SUBMODEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/SUBSET ------------------------------------------------------
@dataclass
class SurfSubset(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/SUBSET` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/SUBSET"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/SURF ------------------------------------------------------
@dataclass
class SurfSurf(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/SURF` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/SURF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TABLE/0 ------------------------------------------------------
@dataclass
class Table0(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TABLE/0` is not implemented.")

    @property
    def keyword(self):
        return "/TABLE/0"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TABLE/1 ------------------------------------------------------
@dataclass
class Table1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TABLE/1` is not implemented.")

    @property
    def keyword(self):
        return "/TABLE/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TETRA4 ------------------------------------------------------
@dataclass
class Tetra4(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TETRA4` is not implemented.")

    @property
    def keyword(self):
        return "/TETRA4"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TETRA10 ------------------------------------------------------
@dataclass
class Tetra10(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TETRA10` is not implemented.")

    @property
    def keyword(self):
        return "/TETRA10"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH ------------------------------------------------------
@dataclass
class Th(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH` is not implemented.")

    @property
    def keyword(self):
        return "/TH"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
