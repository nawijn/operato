#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MAT/LAW87                  /MAT/LAW88                  /MAT/LAW90                  
# /MAT/LAW92                  /MAT/LAW93                  /MAT/LAW94                  
# /MAT/LAW95                  /MAT/LAW97                  /MAT/LAW10                  
#

# --- /MAT/LAW87 ------------------------------------------------------
@dataclass
class MatLaw87(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW87` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW87"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW88 ------------------------------------------------------
@dataclass
class MatLaw88(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW88` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW88"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW90 ------------------------------------------------------
@dataclass
class MatLaw90(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW90` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW90"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW92 ------------------------------------------------------
@dataclass
class MatLaw92(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW92` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW92"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW93 ------------------------------------------------------
@dataclass
class MatLaw93(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW93` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW93"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW94 ------------------------------------------------------
@dataclass
class MatLaw94(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW94` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW94"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW95 ------------------------------------------------------
@dataclass
class MatLaw95(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW95` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW95"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW97 ------------------------------------------------------
@dataclass
class MatLaw97(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW97` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW97"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW10 ------------------------------------------------------
@dataclass
class MatLaw10(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW10` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW10"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
