#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /STATE/BEAM/AUX             /STATE/BEAM/FULL            /STATE/BRICK/AUX/FULL       
# /STATE/BRICK/EREF           /STATE/BRICK/FAIL           /STATE/BRICK/ORTHO          
# /STATE/BRICK/STRAIN/FULL    /STATE/BRICK/STRAIN/GLOBFULL/STATE/BRICK/STRES/FULL     
#

# --- /STATE/BEAM/AUX ------------------------------------------------------
@dataclass
class StateBeamAux(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BEAM/AUX` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BEAM/AUX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/BEAM/FULL ------------------------------------------------------
@dataclass
class StateBeamFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BEAM/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BEAM/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/BRICK/AUX/FULL ------------------------------------------------------
@dataclass
class StateBrickAuxFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BRICK/AUX/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BRICK/AUX/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/BRICK/EREF ------------------------------------------------------
@dataclass
class StateBrickEref(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BRICK/EREF` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BRICK/EREF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/BRICK/FAIL ------------------------------------------------------
@dataclass
class StateBrickFail(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BRICK/FAIL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BRICK/FAIL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/BRICK/ORTHO ------------------------------------------------------
@dataclass
class StateBrickOrtho(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BRICK/ORTHO` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BRICK/ORTHO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/BRICK/STRAIN/FULL ------------------------------------------------------
@dataclass
class StateBrickStrainFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BRICK/STRAIN/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BRICK/STRAIN/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/BRICK/STRAIN/GLOBFULL ------------------------------------------------------
@dataclass
class StateBrickStrainGlobfull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BRICK/STRAIN/GLOBFULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BRICK/STRAIN/GLOBFULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/BRICK/STRES/FULL ------------------------------------------------------
@dataclass
class StateBrickStresFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BRICK/STRES/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BRICK/STRES/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
