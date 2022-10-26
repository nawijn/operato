#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INTER/LAGMUL/TYPE2         /INTER/LAGMUL/TYPE7         /INTER/LAGMUL/TYPE16        
# /INTER/LAGMUL/TYPE17        /INTER/SUB                  /INTER/TYPE1                
# /INTER/TYPE2                /INTER/TYPE3                /INTER/TYPE5                
#

# --- /INTER/LAGMUL/TYPE2 ------------------------------------------------------
@dataclass
class InterLagmulType2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/LAGMUL/TYPE2` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/LAGMUL/TYPE2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/LAGMUL/TYPE7 ------------------------------------------------------
@dataclass
class InterLagmulType7(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/LAGMUL/TYPE7` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/LAGMUL/TYPE7"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/LAGMUL/TYPE16 ------------------------------------------------------
@dataclass
class InterLagmulType16(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/LAGMUL/TYPE16` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/LAGMUL/TYPE16"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/LAGMUL/TYPE17 ------------------------------------------------------
@dataclass
class InterLagmulType17(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/LAGMUL/TYPE17` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/LAGMUL/TYPE17"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/SUB ------------------------------------------------------
@dataclass
class InterSub(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/SUB` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/SUB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE1 ------------------------------------------------------
@dataclass
class InterType1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE1` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE2 ------------------------------------------------------
@dataclass
class InterType2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE2` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE3 ------------------------------------------------------
@dataclass
class InterType3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE3` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE5 ------------------------------------------------------
@dataclass
class InterType5(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE5` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE5"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
