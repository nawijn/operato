#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ALE/LINK/VEL               /ALE/MUSCL/OFF              /ALE/OFF                    
# /ALE/ON                     /ALE/SOLVER/FINT            /ALE/SUPG/OFF               
# /ANIM/BRICK/DAMA            /ANIM/BRICK/Restype         /ANIM/BRICK/TDEL            
#

# --- /ALE/LINK/VEL ------------------------------------------------------
@dataclass
class AleLinkVel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/LINK/VEL` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/LINK/VEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ALE/MUSCL/OFF ------------------------------------------------------
@dataclass
class AleMusclOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/MUSCL/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/MUSCL/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ALE/OFF ------------------------------------------------------
@dataclass
class AleOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ALE/ON ------------------------------------------------------
@dataclass
class AleOn(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/ON` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/ON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ALE/SOLVER/FINT ------------------------------------------------------
@dataclass
class AleSolverFint(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/SOLVER/FINT` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/SOLVER/FINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ALE/SUPG/OFF ------------------------------------------------------
@dataclass
class AleSupgOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/SUPG/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/SUPG/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/BRICK/DAMA ------------------------------------------------------
@dataclass
class AnimBrickDama(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/BRICK/DAMA` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/BRICK/DAMA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/BRICK/Restype ------------------------------------------------------
@dataclass
class AnimBrickRestype(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/BRICK/Restype` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/BRICK/Restype"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/BRICK/TDEL ------------------------------------------------------
@dataclass
class AnimBrickTdel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/BRICK/TDEL` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/BRICK/TDEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
