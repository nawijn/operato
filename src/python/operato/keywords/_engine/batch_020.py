#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PRINT                      /RAD2RAD/ON                 /RBODY                      
# /REPORT                     /RERUN                      /RFILE/OFF                  
# /RFILE/n                    /RUN                        /SHSUB                      
#

# --- /PRINT ------------------------------------------------------
@dataclass
class Print(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PRINT` is not implemented.")

    @property
    def keyword(self):
        return "/PRINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RAD2RAD/ON ------------------------------------------------------
@dataclass
class Rad2radOn(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RAD2RAD/ON` is not implemented.")

    @property
    def keyword(self):
        return "/RAD2RAD/ON"

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


# --- /REPORT ------------------------------------------------------
@dataclass
class Report(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/REPORT` is not implemented.")

    @property
    def keyword(self):
        return "/REPORT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RERUN ------------------------------------------------------
@dataclass
class Rerun(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RERUN` is not implemented.")

    @property
    def keyword(self):
        return "/RERUN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RFILE/OFF ------------------------------------------------------
@dataclass
class RfileOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RFILE/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/RFILE/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RFILE/n ------------------------------------------------------
@dataclass
class RfileN(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RFILE/n` is not implemented.")

    @property
    def keyword(self):
        return "/RFILE/n"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /RUN ------------------------------------------------------
@dataclass
class Run(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RUN` is not implemented.")

    @property
    def keyword(self):
        return "/RUN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /SHSUB ------------------------------------------------------
@dataclass
class Shsub(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SHSUB` is not implemented.")

    @property
    def keyword(self):
        return "/SHSUB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
