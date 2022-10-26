#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /LAGMUL                     /LEAK/MAT                   /LINE                       
# /LOAD/CENTRI                /LOAD/PBLAST                /LOAD/PFLUID                
# /MADYMO/EXFEM               /MAT/B-K-EPS                /MAT/GAS                    
#

# --- /LAGMUL ------------------------------------------------------
@dataclass
class Lagmul(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/LAGMUL` is not implemented.")

    @property
    def keyword(self):
        return "/LAGMUL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /LEAK/MAT ------------------------------------------------------
@dataclass
class LeakMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/LEAK/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/LEAK/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /LINE ------------------------------------------------------
@dataclass
class Line(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/LINE` is not implemented.")

    @property
    def keyword(self):
        return "/LINE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /LOAD/CENTRI ------------------------------------------------------
@dataclass
class LoadCentri(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/LOAD/CENTRI` is not implemented.")

    @property
    def keyword(self):
        return "/LOAD/CENTRI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /LOAD/PBLAST ------------------------------------------------------
@dataclass
class LoadPblast(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/LOAD/PBLAST` is not implemented.")

    @property
    def keyword(self):
        return "/LOAD/PBLAST"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /LOAD/PFLUID ------------------------------------------------------
@dataclass
class LoadPfluid(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/LOAD/PFLUID` is not implemented.")

    @property
    def keyword(self):
        return "/LOAD/PFLUID"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MADYMO/EXFEM ------------------------------------------------------
@dataclass
class MadymoExfem(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MADYMO/EXFEM` is not implemented.")

    @property
    def keyword(self):
        return "/MADYMO/EXFEM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/B-K-EPS ------------------------------------------------------
@dataclass
class MatBKEps(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/B-K-EPS` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/B-K-EPS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/GAS ------------------------------------------------------
@dataclass
class MatGas(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/GAS` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/GAS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
