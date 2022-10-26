#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PROP/TYPE16                /PROP/TYPE17                /PROP/TYPE18                
# /PROP/TYPE19                /PROP/TYPE20                /PROP/TYPE21                
# /PROP/TYPE22                /PROP/TYPE23                /PROP/TYPE25                
#

# --- /PROP/TYPE16 ------------------------------------------------------
@dataclass
class PropType16(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE16` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE16"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE17 ------------------------------------------------------
@dataclass
class PropType17(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE17` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE17"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE18 ------------------------------------------------------
@dataclass
class PropType18(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE18` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE18"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE19 ------------------------------------------------------
@dataclass
class PropType19(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE19` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE19"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE20 ------------------------------------------------------
@dataclass
class PropType20(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE20` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE20"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE21 ------------------------------------------------------
@dataclass
class PropType21(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE21` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE21"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE22 ------------------------------------------------------
@dataclass
class PropType22(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE22` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE22"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE23 ------------------------------------------------------
@dataclass
class PropType23(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE23` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE23"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PROP/TYPE25 ------------------------------------------------------
@dataclass
class PropType25(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE25` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE25"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
