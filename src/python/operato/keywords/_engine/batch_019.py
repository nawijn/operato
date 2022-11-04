#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /KEREL/1                    /KILL                       /MADYMO                     
# /MASS/RESET                 /MON                        /NEGVOL                     
# /OUTP                       /OUTPUT/LSENSOR             /PARITH                     
#

# --- /KEREL/1 ------------------------------------------------------
@dataclass
class Kerel1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/KEREL/1` is not implemented.")

    @property
    def keyword(self):
        return "/KEREL/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /KILL ------------------------------------------------------
@dataclass
class Kill(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/KILL` is not implemented.")

    @property
    def keyword(self):
        return "/KILL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MADYMO ------------------------------------------------------
@dataclass
class Madymo(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MADYMO` is not implemented.")

    @property
    def keyword(self):
        return "/MADYMO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MASS/RESET ------------------------------------------------------
@dataclass
class MassReset(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MASS/RESET` is not implemented.")

    @property
    def keyword(self):
        return "/MASS/RESET"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /MON ------------------------------------------------------
@dataclass
class Mon(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MON` is not implemented.")

    @property
    def keyword(self):
        return "/MON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /NEGVOL ------------------------------------------------------
@dataclass
class Negvol(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/NEGVOL` is not implemented.")

    @property
    def keyword(self):
        return "/NEGVOL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /OUTP ------------------------------------------------------
@dataclass
class Outp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/OUTP` is not implemented.")

    @property
    def keyword(self):
        return "/OUTP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /OUTPUT/LSENSOR ------------------------------------------------------
@dataclass
class OutputLsensor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/OUTPUT/LSENSOR` is not implemented.")

    @property
    def keyword(self):
        return "/OUTPUT/LSENSOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /PARITH ------------------------------------------------------
@dataclass
class Parith(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PARITH` is not implemented.")

    @property
    def keyword(self):
        return "/PARITH"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
