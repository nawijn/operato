#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MAT/LAW112                 /MAT/LAW113                 /MAT/LAW114                 
# /MAT/LAW115                 /MAT/LAW116                 /MAT/LAW117                 
# /MAT/LAW119                 /MAT/LAW121                 /MAT/LAW151                 
#

# --- /MAT/LAW112 ------------------------------------------------------
@dataclass
class MatLaw112(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW112` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW112"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW113 ------------------------------------------------------
@dataclass
class MatLaw113(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW113` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW113"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW114 ------------------------------------------------------
@dataclass
class MatLaw114(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW114` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW114"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW115 ------------------------------------------------------
@dataclass
class MatLaw115(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW115` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW115"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW116 ------------------------------------------------------
@dataclass
class MatLaw116(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW116` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW116"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW117 ------------------------------------------------------
@dataclass
class MatLaw117(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW117` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW117"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW119 ------------------------------------------------------
@dataclass
class MatLaw119(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW119` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW119"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW121 ------------------------------------------------------
@dataclass
class MatLaw121(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW121` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW121"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MAT/LAW151 ------------------------------------------------------
@dataclass
class MatLaw151(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW151` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW151"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
