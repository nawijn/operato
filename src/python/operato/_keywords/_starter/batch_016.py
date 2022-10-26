#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /GRSHEL                     /GRSPRI                     /GRTRIA                     
# /GRTRUS                     /HEAT/MAT                   /IMPACC                     
# /IMPDISP                    /IMPDISP/FGEO               /IMPFLUX                    
#

# --- /GRSHEL ------------------------------------------------------
@dataclass
class Grshel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRSHEL` is not implemented.")

    @property
    def keyword(self):
        return "/GRSHEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRSPRI ------------------------------------------------------
@dataclass
class Grspri(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRSPRI` is not implemented.")

    @property
    def keyword(self):
        return "/GRSPRI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRTRIA ------------------------------------------------------
@dataclass
class Grtria(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRTRIA` is not implemented.")

    @property
    def keyword(self):
        return "/GRTRIA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRTRUS ------------------------------------------------------
@dataclass
class Grtrus(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRTRUS` is not implemented.")

    @property
    def keyword(self):
        return "/GRTRUS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /HEAT/MAT ------------------------------------------------------
@dataclass
class HeatMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/HEAT/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/HEAT/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPACC ------------------------------------------------------
@dataclass
class Impacc(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPACC` is not implemented.")

    @property
    def keyword(self):
        return "/IMPACC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPDISP ------------------------------------------------------
@dataclass
class Impdisp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPDISP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPDISP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPDISP/FGEO ------------------------------------------------------
@dataclass
class ImpdispFgeo(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPDISP/FGEO` is not implemented.")

    @property
    def keyword(self):
        return "/IMPDISP/FGEO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPFLUX ------------------------------------------------------
@dataclass
class Impflux(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPFLUX` is not implemented.")

    @property
    def keyword(self):
        return "/IMPFLUX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
