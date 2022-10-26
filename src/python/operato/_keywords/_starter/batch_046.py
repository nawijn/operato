#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /RANDOM                     /RBE2                       /RBE3                       
# /RBODY                      /RBODY/LAGMUL               /REFSTA                     
# /RETRACTOR/SPRING           /RLINK                      /RWALL                      
#

# --- /RANDOM ------------------------------------------------------
@dataclass
class Random(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RANDOM` is not implemented.")

    @property
    def keyword(self):
        return "/RANDOM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RBE2 ------------------------------------------------------
@dataclass
class Rbe2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RBE2` is not implemented.")

    @property
    def keyword(self):
        return "/RBE2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RBE3 ------------------------------------------------------
@dataclass
class Rbe3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RBE3` is not implemented.")

    @property
    def keyword(self):
        return "/RBE3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RBODY ------------------------------------------------------
@dataclass
class Rbody(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RBODY` is not implemented.")

    @property
    def keyword(self):
        return "/RBODY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RBODY/LAGMUL ------------------------------------------------------
@dataclass
class RbodyLagmul(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RBODY/LAGMUL` is not implemented.")

    @property
    def keyword(self):
        return "/RBODY/LAGMUL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /REFSTA ------------------------------------------------------
@dataclass
class Refsta(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/REFSTA` is not implemented.")

    @property
    def keyword(self):
        return "/REFSTA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RETRACTOR/SPRING ------------------------------------------------------
@dataclass
class RetractorSpring(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RETRACTOR/SPRING` is not implemented.")

    @property
    def keyword(self):
        return "/RETRACTOR/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RLINK ------------------------------------------------------
@dataclass
class Rlink(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RLINK` is not implemented.")

    @property
    def keyword(self):
        return "/RLINK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RWALL ------------------------------------------------------
@dataclass
class Rwall(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RWALL` is not implemented.")

    @property
    def keyword(self):
        return "/RWALL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
