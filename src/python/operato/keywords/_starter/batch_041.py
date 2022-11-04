#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PROP/INJECT1               /PROP/INJECT2               /PROP/PCOMPP                
# /PROP/TYPE0                 /PROP/TYPE1                 /PROP/TYPE2                 
# /PROP/TYPE3                 /PROP/TYPE4                 /PROP/TYPE6                 
#

# --- /PROP/INJECT1 ------------------------------------------------------
@dataclass
class PropInject1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/INJECT1` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/INJECT1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/INJECT2 ------------------------------------------------------
@dataclass
class PropInject2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/INJECT2` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/INJECT2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/PCOMPP ------------------------------------------------------
@dataclass
class PropPcompp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/PCOMPP` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/PCOMPP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE0 ------------------------------------------------------
@dataclass
class PropType0(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE0` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE0"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE1 ------------------------------------------------------
@dataclass
class PropType1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE1` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE2 ------------------------------------------------------
@dataclass
class PropType2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE2` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE3 ------------------------------------------------------
@dataclass
class PropType3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE3` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE4 ------------------------------------------------------
@dataclass
class PropType4(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE4` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE4"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE6 ------------------------------------------------------
@dataclass
class PropType6(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE6` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE6"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
