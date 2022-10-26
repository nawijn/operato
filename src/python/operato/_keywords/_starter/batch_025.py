#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INTER/TYPE18               /INTER/TYPE19               /INTER/TYPE21               
# /INTER/TYPE22               /INTER/TYPE23               /INTER/TYPE24               
# /INTER/TYPE25               /IOFLAG                     /KEY                        
#

# --- /INTER/TYPE18 ------------------------------------------------------
@dataclass
class InterType18(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE18` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE18"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE19 ------------------------------------------------------
@dataclass
class InterType19(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE19` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE19"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE21 ------------------------------------------------------
@dataclass
class InterType21(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE21` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE21"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE22 ------------------------------------------------------
@dataclass
class InterType22(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE22` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE22"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE23 ------------------------------------------------------
@dataclass
class InterType23(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE23` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE23"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE24 ------------------------------------------------------
@dataclass
class InterType24(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE24` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE24"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /INTER/TYPE25 ------------------------------------------------------
@dataclass
class InterType25(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE25` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE25"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /IOFLAG ------------------------------------------------------
@dataclass
class Ioflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/IOFLAG` is not implemented.")

    @property
    def keyword(self):
        return "/IOFLAG"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /KEY ------------------------------------------------------
@dataclass
class Key(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/KEY` is not implemented.")

    @property
    def keyword(self):
        return "/KEY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
