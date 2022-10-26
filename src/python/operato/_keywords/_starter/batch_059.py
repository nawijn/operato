#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /TRANSFORM/TRA              /TRIA                       /TRUSS                      
# /UNIT                       /UPWIND                     /VISC/PRONY                 
# /XELEM                      /XREF                       
#

# --- /TRANSFORM/TRA ------------------------------------------------------
@dataclass
class TransformTra(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRANSFORM/TRA` is not implemented.")

    @property
    def keyword(self):
        return "/TRANSFORM/TRA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TRIA ------------------------------------------------------
@dataclass
class Tria(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRIA` is not implemented.")

    @property
    def keyword(self):
        return "/TRIA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /TRUSS ------------------------------------------------------
@dataclass
class Truss(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TRUSS` is not implemented.")

    @property
    def keyword(self):
        return "/TRUSS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /UNIT ------------------------------------------------------
@dataclass
class Unit(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/UNIT` is not implemented.")

    @property
    def keyword(self):
        return "/UNIT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /UPWIND ------------------------------------------------------
@dataclass
class Upwind(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/UPWIND` is not implemented.")

    @property
    def keyword(self):
        return "/UPWIND"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /VISC/PRONY ------------------------------------------------------
@dataclass
class ViscProny(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/VISC/PRONY` is not implemented.")

    @property
    def keyword(self):
        return "/VISC/PRONY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /XELEM ------------------------------------------------------
@dataclass
class Xelem(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/XELEM` is not implemented.")

    @property
    def keyword(self):
        return "/XELEM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /XREF ------------------------------------------------------
@dataclass
class Xref(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/XREF` is not implemented.")

    @property
    def keyword(self):
        return "/XREF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
