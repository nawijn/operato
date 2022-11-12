#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INISH3/ORTH_LOC            /INISHE/ORTHO               /INISH3/ORTHO               
# /INISHE/SCALE_YLD           /INISH3/SCALE_YLD           /INISPRI/FULL               
# /INISHE/STRA_F              /INISH3/STRA_F              /INISHE_STRA_F/GLOB         
#

# --- /INISH3/ORTH_LOC ------------------------------------------------------
@dataclass
class Inish3OrthLoc(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/ORTH_LOC` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/ORTH_LOC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/ORTHO ------------------------------------------------------
@dataclass
class InisheOrtho(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/ORTHO` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/ORTHO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/ORTHO ------------------------------------------------------
@dataclass
class Inish3Ortho(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/ORTHO` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/ORTHO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/SCALE_YLD ------------------------------------------------------
@dataclass
class InisheScaleYld(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/SCALE_YLD` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/SCALE_YLD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/SCALE_YLD ------------------------------------------------------
@dataclass
class Inish3ScaleYld(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/SCALE_YLD` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/SCALE_YLD"

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


# --- /INISHE/STRA_F ------------------------------------------------------
@dataclass
class InisheStraF(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/STRA_F` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/STRA_F"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/STRA_F ------------------------------------------------------
@dataclass
class Inish3StraF(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/STRA_F` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/STRA_F"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE_STRA_F/GLOB ------------------------------------------------------
@dataclass
class InisheStraFGlob(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE_STRA_F/GLOB` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE_STRA_F/GLOB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
