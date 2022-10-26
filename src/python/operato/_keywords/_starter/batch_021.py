#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INISH3_STRA_F/GLOB         /INISHE/STRS_F              /INISH3/STRS_F              
# /INISHE/STRS_F/GLOB         /INISH3/STRS_F/GLOB         /INISHE/THICK               
# /INISH3/THICK               /INISPRI/FULL               /INISTA                     
#

# --- /INISH3_STRA_F/GLOB ------------------------------------------------------
@dataclass
class Inish3StraFGlob(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3_STRA_F/GLOB` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3_STRA_F/GLOB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/STRS_F ------------------------------------------------------
@dataclass
class InisheStrsF(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/STRS_F` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/STRS_F"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/STRS_F ------------------------------------------------------
@dataclass
class Inish3StrsF(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/STRS_F` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/STRS_F"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/STRS_F/GLOB ------------------------------------------------------
@dataclass
class InisheStrsFGlob(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/STRS_F/GLOB` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/STRS_F/GLOB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/STRS_F/GLOB ------------------------------------------------------
@dataclass
class Inish3StrsFGlob(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/STRS_F/GLOB` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/STRS_F/GLOB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/THICK ------------------------------------------------------
@dataclass
class InisheThick(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/THICK` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/THICK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/THICK ------------------------------------------------------
@dataclass
class Inish3Thick(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/THICK` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/THICK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISPRI/FULL ------------------------------------------------------
@dataclass
class InispriFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISPRI/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/INISPRI/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISTA ------------------------------------------------------
@dataclass
class Inista(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISTA` is not implemented.")

    @property
    def keyword(self):
        return "/INISTA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
