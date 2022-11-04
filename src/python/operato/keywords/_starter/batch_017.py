#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPLICIT                   /IMPTEMP                    /IMPVEL                     
# /IMPVEL/FGEO                /IMPVEL/LAGMUL              /INIBEAM/AUX                
# /INIBEAM/FULL               /INIBRI                     /INICRACK                   
#

# --- /IMPLICIT ------------------------------------------------------
@dataclass
class Implicit(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPLICIT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPLICIT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPTEMP ------------------------------------------------------
@dataclass
class Imptemp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPTEMP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPTEMP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPVEL ------------------------------------------------------
@dataclass
class Impvel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPVEL` is not implemented.")

    @property
    def keyword(self):
        return "/IMPVEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPVEL/FGEO ------------------------------------------------------
@dataclass
class ImpvelFgeo(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPVEL/FGEO` is not implemented.")

    @property
    def keyword(self):
        return "/IMPVEL/FGEO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPVEL/LAGMUL ------------------------------------------------------
@dataclass
class ImpvelLagmul(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPVEL/LAGMUL` is not implemented.")

    @property
    def keyword(self):
        return "/IMPVEL/LAGMUL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIBEAM/AUX ------------------------------------------------------
@dataclass
class InibeamAux(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIBEAM/AUX` is not implemented.")

    @property
    def keyword(self):
        return "/INIBEAM/AUX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIBEAM/FULL ------------------------------------------------------
@dataclass
class InibeamFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIBEAM/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/INIBEAM/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIBRI ------------------------------------------------------
@dataclass
class Inibri(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIBRI` is not implemented.")

    @property
    def keyword(self):
        return "/INIBRI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INICRACK ------------------------------------------------------
@dataclass
class Inicrack(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INICRACK` is not implemented.")

    @property
    def keyword(self):
        return "/INICRACK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
