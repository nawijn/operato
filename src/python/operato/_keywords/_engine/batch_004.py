#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ANIM/SHELL/EPSP            /ANIM/SHELL/FLDF            /ANIM/SHELL/FLDZ            
# /ANIM/SHELL/IDPLY           /ANIM/SHELL/IDPLY/DAMA      /ANIM/SHELL/IDPLY/EPSP      
# /ANIM/SHELL/IDPLY/PHI       /ANIM/SHELL/IDPLY/Restype   /ANIM/SHELL/NXTFACTOR       
#

# --- /ANIM/SHELL/EPSP ------------------------------------------------------
@dataclass
class AnimShellEpsp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/EPSP` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/EPSP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/FLDF ------------------------------------------------------
@dataclass
class AnimShellFldf(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/FLDF` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/FLDF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/FLDZ ------------------------------------------------------
@dataclass
class AnimShellFldz(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/FLDZ` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/FLDZ"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/IDPLY ------------------------------------------------------
@dataclass
class AnimShellIdply(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/IDPLY` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/IDPLY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/IDPLY/DAMA ------------------------------------------------------
@dataclass
class AnimShellIdplyDama(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/IDPLY/DAMA` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/IDPLY/DAMA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/IDPLY/EPSP ------------------------------------------------------
@dataclass
class AnimShellIdplyEpsp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/IDPLY/EPSP` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/IDPLY/EPSP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/IDPLY/PHI ------------------------------------------------------
@dataclass
class AnimShellIdplyPhi(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/IDPLY/PHI` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/IDPLY/PHI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/IDPLY/Restype ------------------------------------------------------
@dataclass
class AnimShellIdplyRestype(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/IDPLY/Restype` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/IDPLY/Restype"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ANIM/SHELL/NXTFACTOR ------------------------------------------------------
@dataclass
class AnimShellNxtfactor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/SHELL/NXTFACTOR` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/NXTFACTOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
