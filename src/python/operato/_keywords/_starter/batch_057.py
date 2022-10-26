#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /TH/TRIA                    /TH/TRUSS                   /THERM_STRESS/MAT           
# /THPART                     /THPART/GRBEAM              /THPART/GRBRIC              
# /THPART/GRQUAD              /THPART/GRSH3N              /THPART/GRSHEL              
#

# --- /TH/TRIA ------------------------------------------------------
@dataclass
class ThTria(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/TRIA` is not implemented.")

    @property
    def keyword(self):
        return "/TH/TRIA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/TRUSS ------------------------------------------------------
@dataclass
class ThTruss(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/TRUSS` is not implemented.")

    @property
    def keyword(self):
        return "/TH/TRUSS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /THERM_STRESS/MAT ------------------------------------------------------
@dataclass
class ThermStressMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THERM_STRESS/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/THERM_STRESS/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /THPART ------------------------------------------------------
@dataclass
class Thpart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THPART` is not implemented.")

    @property
    def keyword(self):
        return "/THPART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /THPART/GRBEAM ------------------------------------------------------
@dataclass
class ThpartGrbeam(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THPART/GRBEAM` is not implemented.")

    @property
    def keyword(self):
        return "/THPART/GRBEAM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /THPART/GRBRIC ------------------------------------------------------
@dataclass
class ThpartGrbric(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THPART/GRBRIC` is not implemented.")

    @property
    def keyword(self):
        return "/THPART/GRBRIC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /THPART/GRQUAD ------------------------------------------------------
@dataclass
class ThpartGrquad(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THPART/GRQUAD` is not implemented.")

    @property
    def keyword(self):
        return "/THPART/GRQUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /THPART/GRSH3N ------------------------------------------------------
@dataclass
class ThpartGrsh3n(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THPART/GRSH3N` is not implemented.")

    @property
    def keyword(self):
        return "/THPART/GRSH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /THPART/GRSHEL ------------------------------------------------------
@dataclass
class ThpartGrshel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THPART/GRSHEL` is not implemented.")

    @property
    def keyword(self):
        return "/THPART/GRSHEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
