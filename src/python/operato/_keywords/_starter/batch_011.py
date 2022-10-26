#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /FAIL/ENERGY                /FAIL/FABRIC                /FAIL/FLD                   
# /FAIL/GENE1                 /FAIL/GURSON                /FAIL/HASHIN                
# /FAIL/HC_DSSE               /FAIL/JOHNSON               /FAIL/LAD_DAMA              
#

# --- /FAIL/ENERGY ------------------------------------------------------
@dataclass
class FailEnergy(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/ENERGY` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/ENERGY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/FABRIC ------------------------------------------------------
@dataclass
class FailFabric(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/FABRIC` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/FABRIC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/FLD ------------------------------------------------------
@dataclass
class FailFld(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/FLD` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/FLD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/GENE1 ------------------------------------------------------
@dataclass
class FailGene1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/GENE1` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/GENE1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/GURSON ------------------------------------------------------
@dataclass
class FailGurson(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/GURSON` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/GURSON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/HASHIN ------------------------------------------------------
@dataclass
class FailHashin(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/HASHIN` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/HASHIN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/HC_DSSE ------------------------------------------------------
@dataclass
class FailHcDsse(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/HC_DSSE` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/HC_DSSE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/JOHNSON ------------------------------------------------------
@dataclass
class FailJohnson(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/JOHNSON` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/JOHNSON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/LAD_DAMA ------------------------------------------------------
@dataclass
class FailLadDama(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/LAD_DAMA` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/LAD_DAMA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
