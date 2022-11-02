#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPL/LSEARCH/n             /IMPL/MONVOL/OFF            /IMPL/NCYCLE/STOP           
# /IMPL/NONLIN/N              /IMPL/NONLIN/SMDISP         /IMPL/NONLIN/SOLVINFO       
# /IMPL/PREPAT                /IMPL/PRINT/LINEAR          /IMPL/PRINT/NONLIN          
#

# --- /IMPL/LSEARCH/n ------------------------------------------------------
@dataclass
class ImplLsearchN(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/LSEARCH/n` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/LSEARCH/n"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/MONVOL/OFF ------------------------------------------------------
@dataclass
class ImplMonvolOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/MONVOL/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/MONVOL/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/NCYCLE/STOP ------------------------------------------------------
@dataclass
class ImplNcycleStop(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/NCYCLE/STOP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/NCYCLE/STOP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/NONLIN/N ------------------------------------------------------
@dataclass
class ImplNonlinN(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/NONLIN/N` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/NONLIN/N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/NONLIN/SMDISP ------------------------------------------------------
@dataclass
class ImplNonlinSmdisp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/NONLIN/SMDISP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/NONLIN/SMDISP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/NONLIN/SOLVINFO ------------------------------------------------------
@dataclass
class ImplNonlinSolvinfo(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/NONLIN/SOLVINFO` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/NONLIN/SOLVINFO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/PREPAT ------------------------------------------------------
@dataclass
class ImplPrepat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/PREPAT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/PREPAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/PRINT/LINEAR ------------------------------------------------------
@dataclass
class ImplPrintLinear(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/PRINT/LINEAR` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/PRINT/LINEAR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/PRINT/NONLIN ------------------------------------------------------
@dataclass
class ImplPrintNonlin(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/PRINT/NONLIN` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/PRINT/NONLIN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
