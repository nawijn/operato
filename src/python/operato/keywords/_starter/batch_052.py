#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SURF/ELLIPS                /SURF/GRBRIC/EXT            /SURF/GRBRIC/FREE           
# /SURF/GRSH3N                /SURF/GRSHEL                /SURF/MAT                   
# /SURF/PART                  /SURF/PLANE                 /SURF/PROP                  
#

# --- /SURF/ELLIPS ------------------------------------------------------
@dataclass
class SurfEllips(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/ELLIPS` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/ELLIPS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/GRBRIC/EXT ------------------------------------------------------
@dataclass
class SurfGrbricExt(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/GRBRIC/EXT` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/GRBRIC/EXT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/GRBRIC/FREE ------------------------------------------------------
@dataclass
class SurfGrbricFree(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/GRBRIC/FREE` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/GRBRIC/FREE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/GRSH3N ------------------------------------------------------
@dataclass
class SurfGrsh3n(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/GRSH3N` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/GRSH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/GRSHEL ------------------------------------------------------
@dataclass
class SurfGrshel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/GRSHEL` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/GRSHEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/MAT ------------------------------------------------------
@dataclass
class SurfMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/PART ------------------------------------------------------
@dataclass
class SurfPart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/PART` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/PART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/PLANE ------------------------------------------------------
@dataclass
class SurfPlane(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/PLANE` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/PLANE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/PROP ------------------------------------------------------
@dataclass
class SurfProp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/PROP` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/PROP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
