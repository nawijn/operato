#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /DT/ALE                     /DT/AMS                     /DT/CST_AMS                 
# /DT/Eltyp/Keyword3/Iflag    /DT/FVMBAG/Iflag            /DT/INTER/Keyword3/Iflag    
# /DT/NODA/Keyword3/Iflag     /DT/SHNOD/Keyword3          /DT/SPHCEL/Keyword3         
#

# --- /DT/ALE ------------------------------------------------------
@dataclass
class DtAle(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/ALE` is not implemented.")

    @property
    def keyword(self):
        return "/DT/ALE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/AMS ------------------------------------------------------
@dataclass
class DtAms(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/AMS` is not implemented.")

    @property
    def keyword(self):
        return "/DT/AMS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/CST_AMS ------------------------------------------------------
@dataclass
class DtCstAms(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/CST_AMS` is not implemented.")

    @property
    def keyword(self):
        return "/DT/CST_AMS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/Eltyp/Keyword3/Iflag ------------------------------------------------------
@dataclass
class DtEltypKeyword3Iflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/Eltyp/Keyword3/Iflag` is not implemented.")

    @property
    def keyword(self):
        return "/DT/Eltyp/Keyword3/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/FVMBAG/Iflag ------------------------------------------------------
@dataclass
class DtFvmbagIflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/FVMBAG/Iflag` is not implemented.")

    @property
    def keyword(self):
        return "/DT/FVMBAG/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/INTER/Keyword3/Iflag ------------------------------------------------------
@dataclass
class DtInterKeyword3Iflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/INTER/Keyword3/Iflag` is not implemented.")

    @property
    def keyword(self):
        return "/DT/INTER/Keyword3/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/NODA/Keyword3/Iflag ------------------------------------------------------
@dataclass
class DtNodaKeyword3Iflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/NODA/Keyword3/Iflag` is not implemented.")

    @property
    def keyword(self):
        return "/DT/NODA/Keyword3/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/SHNOD/Keyword3 ------------------------------------------------------
@dataclass
class DtShnodKeyword3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/SHNOD/Keyword3` is not implemented.")

    @property
    def keyword(self):
        return "/DT/SHNOD/Keyword3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DT/SPHCEL/Keyword3 ------------------------------------------------------
@dataclass
class DtSphcelKeyword3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DT/SPHCEL/Keyword3` is not implemented.")

    @property
    def keyword(self):
        return "/DT/SPHCEL/Keyword3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
