#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /VEL/ROT                    /VEL/TRA                    /VERS                       
#

# --- /VEL/ROT ------------------------------------------------------
@dataclass
class VelRot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/VEL/ROT` is not implemented.")

    @property
    def keyword(self):
        return "/VEL/ROT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /VEL/TRA ------------------------------------------------------
@dataclass
class VelTra(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/VEL/TRA` is not implemented.")

    @property
    def keyword(self):
        return "/VEL/TRA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /VERS ------------------------------------------------------
@dataclass
class Vers(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/VERS` is not implemented.")

    @property
    def keyword(self):
        return "/VERS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
