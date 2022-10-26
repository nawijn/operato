#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INIQUA/STRESS              /INISHE/AUX                 /INISH3/AUX                 
# /INISHE/EPSP                /INISH3/EPSP                /INISHE/EPSP_F              
# /INISH3/EPSP_F              /INISHE/FAIL                /INISHE/ORTH_LOC            
#

# --- /INIQUA/STRESS ------------------------------------------------------
@dataclass
class IniquaStress(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIQUA/STRESS` is not implemented.")

    @property
    def keyword(self):
        return "/INIQUA/STRESS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/AUX ------------------------------------------------------
@dataclass
class InisheAux(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/AUX` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/AUX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/AUX ------------------------------------------------------
@dataclass
class Inish3Aux(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/AUX` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/AUX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/EPSP ------------------------------------------------------
@dataclass
class InisheEpsp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/EPSP` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/EPSP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/EPSP ------------------------------------------------------
@dataclass
class Inish3Epsp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/EPSP` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/EPSP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/EPSP_F ------------------------------------------------------
@dataclass
class InisheEpspF(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/EPSP_F` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/EPSP_F"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISH3/EPSP_F ------------------------------------------------------
@dataclass
class Inish3EpspF(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISH3/EPSP_F` is not implemented.")

    @property
    def keyword(self):
        return "/INISH3/EPSP_F"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/FAIL ------------------------------------------------------
@dataclass
class InisheFail(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/FAIL` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/FAIL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INISHE/ORTH_LOC ------------------------------------------------------
@dataclass
class InisheOrthLoc(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INISHE/ORTH_LOC` is not implemented.")

    @property
    def keyword(self):
        return "/INISHE/ORTH_LOC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
