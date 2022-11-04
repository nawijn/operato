#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PROP/TYPE8                 /PROP/TYPE9                 /PROP/TYPE10                
# /PROP/TYPE11                /PROP/TYPE12                /PROP/TYPE13                
# /PROP/TYPE14                /PROP/TYPE14                /PROP/TYPE15                
#

# --- /PROP/TYPE8 ------------------------------------------------------
@dataclass
class PropType8(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE8` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE8"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE9 ------------------------------------------------------
@dataclass
class PropType9(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE9` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE9"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE10 ------------------------------------------------------
@dataclass
class PropType10(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE10` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE10"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE11 ------------------------------------------------------
@dataclass
class PropType11(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE11` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE11"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE12 ------------------------------------------------------
@dataclass
class PropType12(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE12` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE12"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE13 ------------------------------------------------------
@dataclass
class PropType13(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE13` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE13"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE14 ------------------------------------------------------
@dataclass
class PropType14(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE14` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE14"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE14 ------------------------------------------------------
@dataclass
class PropType14(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE14` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE14"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE15 ------------------------------------------------------
@dataclass
class PropType15(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE15` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE15"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
