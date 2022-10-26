#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /TH/MODE                    /TH/MONVOL                  /TH/NODE                    
# /TH/NSTRAND                 /TH/PART                    /TH/QUAD                    
# /TH/RBODY                   /TH/RETRACTOR               /TH/RWALL                   
#

# --- /TH/MODE ------------------------------------------------------
@dataclass
class ThMode(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/MODE` is not implemented.")

    @property
    def keyword(self):
        return "/TH/MODE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/MONVOL ------------------------------------------------------
@dataclass
class ThMonvol(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/MONVOL` is not implemented.")

    @property
    def keyword(self):
        return "/TH/MONVOL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/NODE ------------------------------------------------------
@dataclass
class ThNode(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/NODE` is not implemented.")

    @property
    def keyword(self):
        return "/TH/NODE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/NSTRAND ------------------------------------------------------
@dataclass
class ThNstrand(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/NSTRAND` is not implemented.")

    @property
    def keyword(self):
        return "/TH/NSTRAND"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/PART ------------------------------------------------------
@dataclass
class ThPart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/PART` is not implemented.")

    @property
    def keyword(self):
        return "/TH/PART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/QUAD ------------------------------------------------------
@dataclass
class ThQuad(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/QUAD` is not implemented.")

    @property
    def keyword(self):
        return "/TH/QUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/RBODY ------------------------------------------------------
@dataclass
class ThRbody(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/RBODY` is not implemented.")

    @property
    def keyword(self):
        return "/TH/RBODY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/RETRACTOR ------------------------------------------------------
@dataclass
class ThRetractor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/RETRACTOR` is not implemented.")

    @property
    def keyword(self):
        return "/TH/RETRACTOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TH/RWALL ------------------------------------------------------
@dataclass
class ThRwall(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH/RWALL` is not implemented.")

    @property
    def keyword(self):
        return "/TH/RWALL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
