#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ATFILE                     /ATSYMBOLFILE               /ATSYMBOLFILE/Keyword2      
# /BCS/ALE                    /BCS/LAG                    /BCS/ROT                    
# /BCS/TRA                    /BCSR/ALE                   /BCSR/LAG                   
#

# --- /ATFILE ------------------------------------------------------
@dataclass
class Atfile(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ATFILE` is not implemented.")

    @property
    def keyword(self):
        return "/ATFILE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ATSYMBOLFILE ------------------------------------------------------
@dataclass
class Atsymbolfile(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ATSYMBOLFILE` is not implemented.")

    @property
    def keyword(self):
        return "/ATSYMBOLFILE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /ATSYMBOLFILE/Keyword2 ------------------------------------------------------
@dataclass
class AtsymbolfileKeyword2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ATSYMBOLFILE/Keyword2` is not implemented.")

    @property
    def keyword(self):
        return "/ATSYMBOLFILE/Keyword2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /BCS/ALE ------------------------------------------------------
@dataclass
class BcsAle(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BCS/ALE` is not implemented.")

    @property
    def keyword(self):
        return "/BCS/ALE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /BCS/LAG ------------------------------------------------------
@dataclass
class BcsLag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BCS/LAG` is not implemented.")

    @property
    def keyword(self):
        return "/BCS/LAG"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /BCS/ROT ------------------------------------------------------
@dataclass
class BcsRot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BCS/ROT` is not implemented.")

    @property
    def keyword(self):
        return "/BCS/ROT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /BCS/TRA ------------------------------------------------------
@dataclass
class BcsTra(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BCS/TRA` is not implemented.")

    @property
    def keyword(self):
        return "/BCS/TRA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /BCSR/ALE ------------------------------------------------------
@dataclass
class BcsrAle(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BCSR/ALE` is not implemented.")

    @property
    def keyword(self):
        return "/BCSR/ALE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /BCSR/LAG ------------------------------------------------------
@dataclass
class BcsrLag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BCSR/LAG` is not implemented.")

    @property
    def keyword(self):
        return "/BCSR/LAG"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
