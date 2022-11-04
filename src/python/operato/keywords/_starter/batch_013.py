#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /FAIL/TAB1                  /FAIL/TBUTCHER              /FAIL/TENSSTRAIN            
# /FAIL/USERi                 /FAIL/VISUAL                /FAIL/WIERZBICKI            
# /FAIL/WILKINS               /FRAME/FIX                  /FRAME/MOV                  
#

# --- /FAIL/TAB1 ------------------------------------------------------
@dataclass
class FailTab1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/TAB1` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/TAB1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/TBUTCHER ------------------------------------------------------
@dataclass
class FailTbutcher(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/TBUTCHER` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/TBUTCHER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/TENSSTRAIN ------------------------------------------------------
@dataclass
class FailTensstrain(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/TENSSTRAIN` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/TENSSTRAIN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/USERi ------------------------------------------------------
@dataclass
class FailUseri(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/USERi` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/USERi"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/VISUAL ------------------------------------------------------
@dataclass
class FailVisual(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/VISUAL` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/VISUAL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/WIERZBICKI ------------------------------------------------------
@dataclass
class FailWierzbicki(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/WIERZBICKI` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/WIERZBICKI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FAIL/WILKINS ------------------------------------------------------
@dataclass
class FailWilkins(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FAIL/WILKINS` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/WILKINS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FRAME/FIX ------------------------------------------------------
@dataclass
class FrameFix(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FRAME/FIX` is not implemented.")

    @property
    def keyword(self):
        return "/FRAME/FIX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FRAME/MOV ------------------------------------------------------
@dataclass
class FrameMov(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FRAME/MOV` is not implemented.")

    @property
    def keyword(self):
        return "/FRAME/MOV"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
