#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MAT/LAW10                  /MAT/LAW11                  /MAT/LAW12                  
# /MAT/LAW14                  /MAT/LAW15                  /MAT/LAW16                  
# /MAT/LAW18                  /MAT/LAW19                  /MAT/LAW20                  
#

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


# --- /MAT/LAW11 ------------------------------------------------------
@dataclass
class MatLaw11(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW11` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW11"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW12 ------------------------------------------------------
@dataclass
class MatLaw12(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW12` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW12"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW14 ------------------------------------------------------
@dataclass
class MatLaw14(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW14` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW14"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW15 ------------------------------------------------------
@dataclass
class MatLaw15(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW15` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW15"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW16 ------------------------------------------------------
@dataclass
class MatLaw16(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW16` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW16"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW18 ------------------------------------------------------
@dataclass
class MatLaw18(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW18` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW18"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW19 ------------------------------------------------------
@dataclass
class MatLaw19(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW19` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW19"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW20 ------------------------------------------------------
@dataclass
class MatLaw20(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW20` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW20"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
