#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MAT/LAW101                 /MAT/LAW102                 /MAT/LAW103                 
# /MAT/LAW104                 /MAT/LAW106                 /MAT/LAW108                 
# /MAT/LAW109                 /MAT/LAW110                 /MAT/LAW111                 
#

# --- /MAT/LAW101 ------------------------------------------------------
@dataclass
class MatLaw101(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW101` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW101"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW102 ------------------------------------------------------
@dataclass
class MatLaw102(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW102` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW102"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW103 ------------------------------------------------------
@dataclass
class MatLaw103(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW103` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW103"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW104 ------------------------------------------------------
@dataclass
class MatLaw104(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW104` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW104"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW106 ------------------------------------------------------
@dataclass
class MatLaw106(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW106` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW106"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW108 ------------------------------------------------------
@dataclass
class MatLaw108(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW108` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW108"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW109 ------------------------------------------------------
@dataclass
class MatLaw109(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW109` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW109"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW110 ------------------------------------------------------
@dataclass
class MatLaw110(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW110` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW110"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW111 ------------------------------------------------------
@dataclass
class MatLaw111(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW111` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW111"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
