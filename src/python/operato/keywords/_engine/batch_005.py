#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ANIM/SHELL/PHI             /ANIM/SHELL/Restype         /ANIM/SHELL/SIG1H           
# /ANIM/SHELL/SIG2H           /ANIM/SHELL/TDEL            /ANIM/SHELL/TENS            
# /ANIM/TITLE                 /ANIM/VECT                  /ANIM/VERS                  
#

# --- /ANIM/SHELL/PHI ------------------------------------------------------
@dataclass
class AnimShellPhi(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/PHI` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/PHI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/Restype ------------------------------------------------------
@dataclass
class AnimShellRestype(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/Restype` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/Restype"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/SIG1H ------------------------------------------------------
@dataclass
class AnimShellSig1h(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/SIG1H` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/SIG1H"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/SIG2H ------------------------------------------------------
@dataclass
class AnimShellSig2h(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/SIG2H` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/SIG2H"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/TDEL ------------------------------------------------------
@dataclass
class AnimShellTdel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/TDEL` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/TDEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/TENS ------------------------------------------------------
@dataclass
class AnimShellTens(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/TENS` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/TENS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/TITLE ------------------------------------------------------
@dataclass
class AnimTitle(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/TITLE` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/TITLE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/VECT ------------------------------------------------------
@dataclass
class AnimVect(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/VECT` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/VECT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/VERS ------------------------------------------------------
@dataclass
class AnimVers(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/VERS` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/VERS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
