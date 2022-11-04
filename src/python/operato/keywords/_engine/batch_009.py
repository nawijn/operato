#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /DT/THERM                   /DT1/BRICK/Keyword3/Iflag   /DT1/SHELL                  
# /DT1TET10                   /DTIX                       /DTSDE                      
# /DTTSH                      /DYNAIN/DT                  /DYNAIN/SHELL/STRAIN/FULL   
#

# --- /DT/THERM ------------------------------------------------------
@dataclass
class DtTherm(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/THERM` is not implemented.")

    @property
    def keyword(self):
        return "/DT/THERM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT1/BRICK/Keyword3/Iflag ------------------------------------------------------
@dataclass
class Dt1BrickKeyword3Iflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT1/BRICK/Keyword3/Iflag` is not implemented.")

    @property
    def keyword(self):
        return "/DT1/BRICK/Keyword3/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT1/SHELL ------------------------------------------------------
@dataclass
class Dt1Shell(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT1/SHELL` is not implemented.")

    @property
    def keyword(self):
        return "/DT1/SHELL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT1TET10 ------------------------------------------------------
@dataclass
class Dt1tet10(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT1TET10` is not implemented.")

    @property
    def keyword(self):
        return "/DT1TET10"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DTIX ------------------------------------------------------
@dataclass
class Dtix(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DTIX` is not implemented.")

    @property
    def keyword(self):
        return "/DTIX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DTSDE ------------------------------------------------------
@dataclass
class Dtsde(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DTSDE` is not implemented.")

    @property
    def keyword(self):
        return "/DTSDE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DTTSH ------------------------------------------------------
@dataclass
class Dttsh(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DTTSH` is not implemented.")

    @property
    def keyword(self):
        return "/DTTSH"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DYNAIN/DT ------------------------------------------------------
@dataclass
class DynainDt(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DYNAIN/DT` is not implemented.")

    @property
    def keyword(self):
        return "/DYNAIN/DT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DYNAIN/SHELL/STRAIN/FULL ------------------------------------------------------
@dataclass
class DynainShellStrainFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DYNAIN/SHELL/STRAIN/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/DYNAIN/SHELL/STRAIN/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
