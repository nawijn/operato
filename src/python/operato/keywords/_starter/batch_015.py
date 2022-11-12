#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /GAUGE/SPH                  /GJOINT                     /GRAV                       
# /GRBEAM                     /GRBRIC                     /GRNOD                      
# /GRPART                     /GRQUAD                     /GRSH3N                     
#

# --- /GAUGE/SPH ------------------------------------------------------
@dataclass
class GaugeSph(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GAUGE/SPH` is not implemented.")

    @property
    def keyword(self):
        return "/GAUGE/SPH"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GJOINT ------------------------------------------------------
@dataclass
class Gjoint(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GJOINT` is not implemented.")

    @property
    def keyword(self):
        return "/GJOINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRAV ------------------------------------------------------
@dataclass
class Grav(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRAV` is not implemented.")

    @property
    def keyword(self):
        return "/GRAV"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRBEAM ------------------------------------------------------
@dataclass
class Grbeam(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRBEAM` is not implemented.")

    @property
    def keyword(self):
        return "/GRBEAM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRBRIC ------------------------------------------------------
@dataclass
class Grbric(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRBRIC` is not implemented.")

    @property
    def keyword(self):
        return "/GRBRIC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRNOD ------------------------------------------------------
@dataclass
class Grnod(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRNOD` is not implemented.")

    @property
    def keyword(self):
        return "/GRNOD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRPART ------------------------------------------------------
@dataclass
class Grpart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRPART` is not implemented.")

    @property
    def keyword(self):
        return "/GRPART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRQUAD ------------------------------------------------------
@dataclass
class Grquad(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRQUAD` is not implemented.")

    @property
    def keyword(self):
        return "/GRQUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /GRSH3N ------------------------------------------------------
@dataclass
class Grsh3n(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/GRSH3N` is not implemented.")

    @property
    def keyword(self):
        return "/GRSH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
