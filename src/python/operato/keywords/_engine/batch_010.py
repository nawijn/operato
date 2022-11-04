#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /DYNAIN/SHELL/STRESS/FULL   /DYREL                      /DYREL/1                    
# /END/ENGINE                 /FUNCT                      /FVMBAG/MODIF               
# /FXINP                      /H3D/BEAM                   /H3D/COMPRESS               
#

# --- /DYNAIN/SHELL/STRESS/FULL ------------------------------------------------------
@dataclass
class DynainShellStressFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DYNAIN/SHELL/STRESS/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/DYNAIN/SHELL/STRESS/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DYREL ------------------------------------------------------
@dataclass
class Dyrel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DYREL` is not implemented.")

    @property
    def keyword(self):
        return "/DYREL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DYREL/1 ------------------------------------------------------
@dataclass
class Dyrel1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DYREL/1` is not implemented.")

    @property
    def keyword(self):
        return "/DYREL/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /END/ENGINE ------------------------------------------------------
@dataclass
class EndEngine(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/END/ENGINE` is not implemented.")

    @property
    def keyword(self):
        return "/END/ENGINE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FUNCT ------------------------------------------------------
@dataclass
class Funct(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FUNCT` is not implemented.")

    @property
    def keyword(self):
        return "/FUNCT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FVMBAG/MODIF ------------------------------------------------------
@dataclass
class FvmbagModif(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FVMBAG/MODIF` is not implemented.")

    @property
    def keyword(self):
        return "/FVMBAG/MODIF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /FXINP ------------------------------------------------------
@dataclass
class Fxinp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/FXINP` is not implemented.")

    @property
    def keyword(self):
        return "/FXINP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/BEAM ------------------------------------------------------
@dataclass
class H3dBeam(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/BEAM` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/BEAM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /H3D/COMPRESS ------------------------------------------------------
@dataclass
class H3dCompress(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/H3D/COMPRESS` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/COMPRESS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
