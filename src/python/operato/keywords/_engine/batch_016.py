#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPL/PSTIF/OFF             /IMPL/QSTAT                 /IMPL/QSTAT/DTSCAL          
# /IMPL/QSTAT/MRIGM           /IMPL/RREF/INTERF/n         /IMPL/RREF/LIMIT            
# /IMPL/RREF/OFF              /IMPL/SBCS/MSGLV            /IMPL/SBCS/ORDER            
#

# --- /IMPL/PSTIF/OFF ------------------------------------------------------
@dataclass
class ImplPstifOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/PSTIF/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/PSTIF/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/QSTAT ------------------------------------------------------
@dataclass
class ImplQstat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/QSTAT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/QSTAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/QSTAT/DTSCAL ------------------------------------------------------
@dataclass
class ImplQstatDtscal(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/QSTAT/DTSCAL` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/QSTAT/DTSCAL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/QSTAT/MRIGM ------------------------------------------------------
@dataclass
class ImplQstatMrigm(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/QSTAT/MRIGM` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/QSTAT/MRIGM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/RREF/INTERF/n ------------------------------------------------------
@dataclass
class ImplRrefInterfN(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/RREF/INTERF/n` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/RREF/INTERF/n"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/RREF/LIMIT ------------------------------------------------------
@dataclass
class ImplRrefLimit(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/RREF/LIMIT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/RREF/LIMIT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/RREF/OFF ------------------------------------------------------
@dataclass
class ImplRrefOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/RREF/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/RREF/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/SBCS/MSGLV ------------------------------------------------------
@dataclass
class ImplSbcsMsglv(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/SBCS/MSGLV` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/SBCS/MSGLV"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IMPL/SBCS/ORDER ------------------------------------------------------
@dataclass
class ImplSbcsOrder(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IMPL/SBCS/ORDER` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/SBCS/ORDER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
