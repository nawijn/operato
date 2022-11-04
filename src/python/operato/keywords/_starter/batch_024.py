#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INTER/TYPE6                /INTER/TYPE7                /INTER/TYPE8                
# /INTER/TYPE9                /INTER/TYPE10               /INTER/TYPE11               
# /INTER/TYPE12               /INTER/TYPE14               /INTER/TYPE15               
#

# --- /INTER/TYPE6 ------------------------------------------------------
@dataclass
class InterType6(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE6` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE6"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE7 ------------------------------------------------------
@dataclass
class InterType7(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE7` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE7"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE8 ------------------------------------------------------
@dataclass
class InterType8(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE8` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE8"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE9 ------------------------------------------------------
@dataclass
class InterType9(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE9` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE9"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE10 ------------------------------------------------------
@dataclass
class InterType10(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE10` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE10"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE11 ------------------------------------------------------
@dataclass
class InterType11(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE11` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE11"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE12 ------------------------------------------------------
@dataclass
class InterType12(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE12` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE12"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE14 ------------------------------------------------------
@dataclass
class InterType14(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE14` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE14"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE15 ------------------------------------------------------
@dataclass
class InterType15(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE15` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE15"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
