#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPL/DIVERG/n              /IMPL/DT/1                  /IMPL/DT/2                  
# /IMPL/DT/3                  /IMPL/DT/FIXPOINT           /IMPL/DT/STOP               
# /IMPL/DTINI                 /IMPL/DYNA/1                /IMPL/DYNA/2                
#

# --- /IMPL/DIVERG/n ------------------------------------------------------
@dataclass
class ImplDivergN(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DIVERG/n` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DIVERG/n"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/DT/1 ------------------------------------------------------
@dataclass
class ImplDt1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DT/1` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/DT/2 ------------------------------------------------------
@dataclass
class ImplDt2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DT/2` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/DT/3 ------------------------------------------------------
@dataclass
class ImplDt3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DT/3` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/DT/FIXPOINT ------------------------------------------------------
@dataclass
class ImplDtFixpoint(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DT/FIXPOINT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/FIXPOINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/DT/STOP ------------------------------------------------------
@dataclass
class ImplDtStop(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DT/STOP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/STOP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/DTINI ------------------------------------------------------
@dataclass
class ImplDtini(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DTINI` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DTINI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/DYNA/1 ------------------------------------------------------
@dataclass
class ImplDyna1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DYNA/1` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DYNA/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/DYNA/2 ------------------------------------------------------
@dataclass
class ImplDyna2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DYNA/2` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DYNA/2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
