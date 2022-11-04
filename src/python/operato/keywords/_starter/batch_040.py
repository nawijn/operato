#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PART                       /PENTA6                     /PERTURB                    
# /PERTURB/FAIL/BIQUAD        /PERTURB/PART/SHELL         /PERTURB/PART/SOLID         
# /PLOAD                      /PLY                        /PRELOAD                    
#

# --- /PART ------------------------------------------------------
@dataclass
class Part(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PART` is not implemented.")

    @property
    def keyword(self):
        return "/PART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PENTA6 ------------------------------------------------------
@dataclass
class Penta6(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PENTA6` is not implemented.")

    @property
    def keyword(self):
        return "/PENTA6"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PERTURB ------------------------------------------------------
@dataclass
class Perturb(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PERTURB` is not implemented.")

    @property
    def keyword(self):
        return "/PERTURB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PERTURB/FAIL/BIQUAD ------------------------------------------------------
@dataclass
class PerturbFailBiquad(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PERTURB/FAIL/BIQUAD` is not implemented.")

    @property
    def keyword(self):
        return "/PERTURB/FAIL/BIQUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PERTURB/PART/SHELL ------------------------------------------------------
@dataclass
class PerturbPartShell(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PERTURB/PART/SHELL` is not implemented.")

    @property
    def keyword(self):
        return "/PERTURB/PART/SHELL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PERTURB/PART/SOLID ------------------------------------------------------
@dataclass
class PerturbPartSolid(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PERTURB/PART/SOLID` is not implemented.")

    @property
    def keyword(self):
        return "/PERTURB/PART/SOLID"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PLOAD ------------------------------------------------------
@dataclass
class Pload(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PLOAD` is not implemented.")

    @property
    def keyword(self):
        return "/PLOAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PLY ------------------------------------------------------
@dataclass
class Ply(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PLY` is not implemented.")

    @property
    def keyword(self):
        return "/PLY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PRELOAD ------------------------------------------------------
@dataclass
class Preload(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PRELOAD` is not implemented.")

    @property
    def keyword(self):
        return "/PRELOAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
