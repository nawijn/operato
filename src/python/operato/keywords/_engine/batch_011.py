#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /H3D/DT                     /H3D/LSENSOR                /H3D/NODA                   
# /H3D/PART                   /H3D/QUAD                   /H3D/RBE2/SINGLE_PART       
# /H3D/RBE3/SINGLE_PART       /H3D/RBODY/SINGLE_PART      /H3D/SHELL                  
#

# --- /H3D/DT ------------------------------------------------------
@dataclass
class H3dDt(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/DT` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/DT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/LSENSOR ------------------------------------------------------
@dataclass
class H3dLsensor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/LSENSOR` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/LSENSOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/NODA ------------------------------------------------------
@dataclass
class H3dNoda(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/NODA` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/NODA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/PART ------------------------------------------------------
@dataclass
class H3dPart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/PART` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/PART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/QUAD ------------------------------------------------------
@dataclass
class H3dQuad(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/QUAD` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/QUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/RBE2/SINGLE_PART ------------------------------------------------------
@dataclass
class H3dRbe2SinglePart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/RBE2/SINGLE_PART` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/RBE2/SINGLE_PART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/RBE3/SINGLE_PART ------------------------------------------------------
@dataclass
class H3dRbe3SinglePart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/RBE3/SINGLE_PART` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/RBE3/SINGLE_PART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/RBODY/SINGLE_PART ------------------------------------------------------
@dataclass
class H3dRbodySinglePart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/RBODY/SINGLE_PART` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/RBODY/SINGLE_PART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/SHELL ------------------------------------------------------
@dataclass
class H3dShell(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/SHELL` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/SHELL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
