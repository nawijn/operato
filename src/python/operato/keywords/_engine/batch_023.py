#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /STATE/SHELL/AUX/FULL       /STATE/SHELL/EPSP/FULL      /STATE/SHELL/FAIL           
# /STATE/SHELL/ORTHL          /STATE/SHELL/STRAIN/FULL    /STATE/SHELL/STRAIN/GLOBFULL
# /STATE/SHELL/STRESS/FULL    /STATE/SHELL/STRESS/GLOBFULL/STATE/SHELL/THICK          
#

# --- /STATE/SHELL/AUX/FULL ------------------------------------------------------
@dataclass
class StateShellAuxFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/AUX/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/AUX/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/SHELL/EPSP/FULL ------------------------------------------------------
@dataclass
class StateShellEpspFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/EPSP/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/EPSP/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/SHELL/FAIL ------------------------------------------------------
@dataclass
class StateShellFail(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/FAIL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/FAIL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/SHELL/ORTHL ------------------------------------------------------
@dataclass
class StateShellOrthl(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/ORTHL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/ORTHL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/SHELL/STRAIN/FULL ------------------------------------------------------
@dataclass
class StateShellStrainFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/STRAIN/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/STRAIN/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/SHELL/STRAIN/GLOBFULL ------------------------------------------------------
@dataclass
class StateShellStrainGlobfull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/STRAIN/GLOBFULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/STRAIN/GLOBFULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/SHELL/STRESS/FULL ------------------------------------------------------
@dataclass
class StateShellStressFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/STRESS/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/STRESS/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/SHELL/STRESS/GLOBFULL ------------------------------------------------------
@dataclass
class StateShellStressGlobfull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/STRESS/GLOBFULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/STRESS/GLOBFULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/SHELL/THICK ------------------------------------------------------
@dataclass
class StateShellThick(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/SHELL/THICK` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SHELL/THICK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
