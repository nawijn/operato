#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /EOS/MURNAGHAN              /EOS/NASG                   /EOS/NOBLE-ABEL             
# /EOS/OSBORNE                /EOS/POLYNOMIAL             /EOS/PUFF                   
# /EOS/SESAME                 /EOS/STIFF-GAS              /EOS/TILLOTSON              
#

# --- /EOS/MURNAGHAN ------------------------------------------------------
@dataclass
class EosMurnaghan(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/MURNAGHAN` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/MURNAGHAN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EOS/NASG ------------------------------------------------------
@dataclass
class EosNasg(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/NASG` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/NASG"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EOS/NOBLE-ABEL ------------------------------------------------------
@dataclass
class EosNobleAbel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/NOBLE-ABEL` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/NOBLE-ABEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EOS/OSBORNE ------------------------------------------------------
@dataclass
class EosOsborne(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/OSBORNE` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/OSBORNE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EOS/POLYNOMIAL ------------------------------------------------------
@dataclass
class EosPolynomial(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/POLYNOMIAL` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/POLYNOMIAL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EOS/PUFF ------------------------------------------------------
@dataclass
class EosPuff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/PUFF` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/PUFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EOS/SESAME ------------------------------------------------------
@dataclass
class EosSesame(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/SESAME` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/SESAME"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EOS/STIFF-GAS ------------------------------------------------------
@dataclass
class EosStiffGas(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/STIFF-GAS` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/STIFF-GAS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EOS/TILLOTSON ------------------------------------------------------
@dataclass
class EosTillotson(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/TILLOTSON` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/TILLOTSON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
