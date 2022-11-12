#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /BCSR/ROT                   /BCSR/TRA                   /DAMP                       
# /DEL                        /DEL/Eltyp/1                /DEL/INTER                  
# /DELINT                     /DT                         /DT/AIRBAG/Keyword3         
#

# --- /BCSR/ROT ------------------------------------------------------
@dataclass
class BcsrRot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BCSR/ROT` is not implemented.")

    @property
    def keyword(self):
        return "/BCSR/ROT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /BCSR/TRA ------------------------------------------------------
@dataclass
class BcsrTra(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BCSR/TRA` is not implemented.")

    @property
    def keyword(self):
        return "/BCSR/TRA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DAMP ------------------------------------------------------
@dataclass
class Damp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DAMP` is not implemented.")

    @property
    def keyword(self):
        return "/DAMP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DEL ------------------------------------------------------
@dataclass
class Del(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DEL` is not implemented.")

    @property
    def keyword(self):
        return "/DEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DEL/Eltyp/1 ------------------------------------------------------
@dataclass
class DelEltyp1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DEL/Eltyp/1` is not implemented.")

    @property
    def keyword(self):
        return "/DEL/Eltyp/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DEL/INTER ------------------------------------------------------
@dataclass
class DelInter(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DEL/INTER` is not implemented.")

    @property
    def keyword(self):
        return "/DEL/INTER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DELINT ------------------------------------------------------
@dataclass
class Delint(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DELINT` is not implemented.")

    @property
    def keyword(self):
        return "/DELINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT ------------------------------------------------------
@dataclass
class Dt(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT` is not implemented.")

    @property
    def keyword(self):
        return "/DT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/AIRBAG/Keyword3 ------------------------------------------------------
@dataclass
class DtAirbagKeyword3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/AIRBAG/Keyword3` is not implemented.")

    @property
    def keyword(self):
        return "/DT/AIRBAG/Keyword3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
