#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SPRING                     /STACK                      /STAMPING                   
# /STATE/STR_FILE             //SUBMODEL                  /SUBSET                     
# /SURF                       /SURF/BOX                   /SURF/DSURF                 
#

# --- /SPRING ------------------------------------------------------
@dataclass
class Spring(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SPRING` is not implemented.")

    @property
    def keyword(self):
        return "/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STACK ------------------------------------------------------
@dataclass
class Stack(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STACK` is not implemented.")

    @property
    def keyword(self):
        return "/STACK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STAMPING ------------------------------------------------------
@dataclass
class Stamping(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STAMPING` is not implemented.")

    @property
    def keyword(self):
        return "/STAMPING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/STR_FILE ------------------------------------------------------
@dataclass
class StateStrFile(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/STR_FILE` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/STR_FILE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- //SUBMODEL ------------------------------------------------------
@dataclass
class Submodel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `//SUBMODEL` is not implemented.")

    @property
    def keyword(self):
        return "//SUBMODEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SUBSET ------------------------------------------------------
@dataclass
class Subset(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SUBSET` is not implemented.")

    @property
    def keyword(self):
        return "/SUBSET"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF ------------------------------------------------------
@dataclass
class Surf(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF` is not implemented.")

    @property
    def keyword(self):
        return "/SURF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/BOX ------------------------------------------------------
@dataclass
class SurfBox(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/BOX` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/BOX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SURF/DSURF ------------------------------------------------------
@dataclass
class SurfDsurf(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/DSURF` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/DSURF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
