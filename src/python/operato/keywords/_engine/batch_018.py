#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INIV/AXIS/Keyword3/2       /INIV/ROT                   /INIV/ROT/Keyword3/1        
# /INIV/ROT/Keyword3/2        /INIV/TRA                   /INIV/TRA/Keyword3/1        
# /INIV/TRA/Keyword3/2        /INTER                      /KEREL                      
#

# --- /INIV/AXIS/Keyword3/2 ------------------------------------------------------
@dataclass
class InivAxisKeyword32(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIV/AXIS/Keyword3/2` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/AXIS/Keyword3/2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIV/ROT ------------------------------------------------------
@dataclass
class InivRot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIV/ROT` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/ROT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIV/ROT/Keyword3/1 ------------------------------------------------------
@dataclass
class InivRotKeyword31(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIV/ROT/Keyword3/1` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/ROT/Keyword3/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIV/ROT/Keyword3/2 ------------------------------------------------------
@dataclass
class InivRotKeyword32(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIV/ROT/Keyword3/2` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/ROT/Keyword3/2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIV/TRA ------------------------------------------------------
@dataclass
class InivTra(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIV/TRA` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/TRA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIV/TRA/Keyword3/1 ------------------------------------------------------
@dataclass
class InivTraKeyword31(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIV/TRA/Keyword3/1` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/TRA/Keyword3/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIV/TRA/Keyword3/2 ------------------------------------------------------
@dataclass
class InivTraKeyword32(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIV/TRA/Keyword3/2` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/TRA/Keyword3/2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER ------------------------------------------------------
@dataclass
class Inter(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER` is not implemented.")

    @property
    def keyword(self):
        return "/INTER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /KEREL ------------------------------------------------------
@dataclass
class Kerel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/KEREL` is not implemented.")

    @property
    def keyword(self):
        return "/KEREL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
