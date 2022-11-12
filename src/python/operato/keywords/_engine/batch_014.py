#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPL/DYNA/DAMP             /IMPL/GSTIF/OFF             /IMPL/INTER/KCOMP           
# /IMPL/INTER/KNONL           /IMPL/LBFGS/L               /IMPL/LINEAR                
# /IMPL/LINEAR/INTER          /IMPL/LRIGROT               /IMPL/LSEARCH/OFF           
#

# --- /IMPL/DYNA/DAMP ------------------------------------------------------
@dataclass
class ImplDynaDamp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/DYNA/DAMP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DYNA/DAMP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/GSTIF/OFF ------------------------------------------------------
@dataclass
class ImplGstifOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/GSTIF/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/GSTIF/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/INTER/KCOMP ------------------------------------------------------
@dataclass
class ImplInterKcomp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/INTER/KCOMP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/INTER/KCOMP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/INTER/KNONL ------------------------------------------------------
@dataclass
class ImplInterKnonl(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/INTER/KNONL` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/INTER/KNONL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/LBFGS/L ------------------------------------------------------
@dataclass
class ImplLbfgsL(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/LBFGS/L` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/LBFGS/L"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/LINEAR ------------------------------------------------------
@dataclass
class ImplLinear(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/LINEAR` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/LINEAR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/LINEAR/INTER ------------------------------------------------------
@dataclass
class ImplLinearInter(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/LINEAR/INTER` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/LINEAR/INTER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/LRIGROT ------------------------------------------------------
@dataclass
class ImplLrigrot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/LRIGROT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/LRIGROT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/LSEARCH/OFF ------------------------------------------------------
@dataclass
class ImplLsearchOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/LSEARCH/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/LSEARCH/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
