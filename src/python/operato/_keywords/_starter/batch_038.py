#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MAT/LAW200                 /MAT/PLAS_PREDEF            /MAT/USERij                 
# /MERGE/RBODY                /MONVOL/AIRBAG1             /MONVOL/AREA                
# /MONVOL/COMMU1              /MONVOL/FVMBAG1             /MONVOL/FVMBAG2             
#

# --- /MAT/LAW200 ------------------------------------------------------
@dataclass
class MatLaw200(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW200` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW200"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/PLAS_PREDEF ------------------------------------------------------
@dataclass
class MatPlasPredef(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/PLAS_PREDEF` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/PLAS_PREDEF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/USERij ------------------------------------------------------
@dataclass
class MatUserij(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/USERij` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/USERij"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MERGE/RBODY ------------------------------------------------------
@dataclass
class MergeRbody(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MERGE/RBODY` is not implemented.")

    @property
    def keyword(self):
        return "/MERGE/RBODY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MONVOL/AIRBAG1 ------------------------------------------------------
@dataclass
class MonvolAirbag1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MONVOL/AIRBAG1` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/AIRBAG1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MONVOL/AREA ------------------------------------------------------
@dataclass
class MonvolArea(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MONVOL/AREA` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/AREA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MONVOL/COMMU1 ------------------------------------------------------
@dataclass
class MonvolCommu1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MONVOL/COMMU1` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/COMMU1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MONVOL/FVMBAG1 ------------------------------------------------------
@dataclass
class MonvolFvmbag1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MONVOL/FVMBAG1` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/FVMBAG1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MONVOL/FVMBAG2 ------------------------------------------------------
@dataclass
class MonvolFvmbag2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MONVOL/FVMBAG2` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/FVMBAG2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
