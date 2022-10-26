#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INITEMP                    /INITRUSS/FULL              /INIVEL                     
# /INIVEL/AXIS                /INIVEL/FVM                 /INIVEL/NODE                
# /INIVOL                     /INTER/HERTZ/TYPE17         /INTER/LAGDT/TYPE7          
#

# --- /INITEMP ------------------------------------------------------
@dataclass
class Initemp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INITEMP` is not implemented.")

    @property
    def keyword(self):
        return "/INITEMP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INITRUSS/FULL ------------------------------------------------------
@dataclass
class InitrussFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INITRUSS/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/INITRUSS/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIVEL ------------------------------------------------------
@dataclass
class Inivel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIVEL` is not implemented.")

    @property
    def keyword(self):
        return "/INIVEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIVEL/AXIS ------------------------------------------------------
@dataclass
class InivelAxis(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIVEL/AXIS` is not implemented.")

    @property
    def keyword(self):
        return "/INIVEL/AXIS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIVEL/FVM ------------------------------------------------------
@dataclass
class InivelFvm(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIVEL/FVM` is not implemented.")

    @property
    def keyword(self):
        return "/INIVEL/FVM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIVEL/NODE ------------------------------------------------------
@dataclass
class InivelNode(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIVEL/NODE` is not implemented.")

    @property
    def keyword(self):
        return "/INIVEL/NODE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INIVOL ------------------------------------------------------
@dataclass
class Inivol(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INIVOL` is not implemented.")

    @property
    def keyword(self):
        return "/INIVOL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/HERTZ/TYPE17 ------------------------------------------------------
@dataclass
class InterHertzType17(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/HERTZ/TYPE17` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/HERTZ/TYPE17"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/LAGDT/TYPE7 ------------------------------------------------------
@dataclass
class InterLagdtType7(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/LAGDT/TYPE7` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/LAGDT/TYPE7"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
