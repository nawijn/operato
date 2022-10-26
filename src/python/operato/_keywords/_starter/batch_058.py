#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /THPART/GRSPRI              /THPART/GRTRUS              /TITLE                      
# /TRANSFORM                  /TRANSFORM/MATRIX           /TRANSFORM/POSITION         
# /TRANSFORM/ROT              /TRANSFORM/SCA              /TRANSFORM/SYM              
#

# --- /THPART/GRSPRI ------------------------------------------------------
@dataclass
class ThpartGrspri(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THPART/GRSPRI` is not implemented.")

    @property
    def keyword(self):
        return "/THPART/GRSPRI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /THPART/GRTRUS ------------------------------------------------------
@dataclass
class ThpartGrtrus(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/THPART/GRTRUS` is not implemented.")

    @property
    def keyword(self):
        return "/THPART/GRTRUS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TITLE ------------------------------------------------------
@dataclass
class Title(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TITLE` is not implemented.")

    @property
    def keyword(self):
        return "/TITLE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TRANSFORM ------------------------------------------------------
@dataclass
class Transform(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRANSFORM` is not implemented.")

    @property
    def keyword(self):
        return "/TRANSFORM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TRANSFORM/MATRIX ------------------------------------------------------
@dataclass
class TransformMatrix(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRANSFORM/MATRIX` is not implemented.")

    @property
    def keyword(self):
        return "/TRANSFORM/MATRIX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TRANSFORM/POSITION ------------------------------------------------------
@dataclass
class TransformPosition(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRANSFORM/POSITION` is not implemented.")

    @property
    def keyword(self):
        return "/TRANSFORM/POSITION"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TRANSFORM/ROT ------------------------------------------------------
@dataclass
class TransformRot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRANSFORM/ROT` is not implemented.")

    @property
    def keyword(self):
        return "/TRANSFORM/ROT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TRANSFORM/SCA ------------------------------------------------------
@dataclass
class TransformSca(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRANSFORM/SCA` is not implemented.")

    @property
    def keyword(self):
        return "/TRANSFORM/SCA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TRANSFORM/SYM ------------------------------------------------------
@dataclass
class TransformSym(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRANSFORM/SYM` is not implemented.")

    @property
    def keyword(self):
        return "/TRANSFORM/SYM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
