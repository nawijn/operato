#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /DFS/DETPLAN/NODE           /DFS/DETPOINT               /DFS/DETPOINT/NODE          
# /DFS/LASER                  /DFS/WAV_SHA                /DRAPE                      
# /EBCS/FLUXOUT               /EBCS/GRADP0                /EBCS/INIP                  
#

# --- /DFS/DETPLAN/NODE ------------------------------------------------------
@dataclass
class DfsDetplanNode(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/DETPLAN/NODE` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/DETPLAN/NODE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DFS/DETPOINT ------------------------------------------------------
@dataclass
class DfsDetpoint(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/DETPOINT` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/DETPOINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DFS/DETPOINT/NODE ------------------------------------------------------
@dataclass
class DfsDetpointNode(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/DETPOINT/NODE` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/DETPOINT/NODE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DFS/LASER ------------------------------------------------------
@dataclass
class DfsLaser(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/LASER` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/LASER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DFS/WAV_SHA ------------------------------------------------------
@dataclass
class DfsWavSha(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/WAV_SHA` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/WAV_SHA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DRAPE ------------------------------------------------------
@dataclass
class Drape(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DRAPE` is not implemented.")

    @property
    def keyword(self):
        return "/DRAPE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EBCS/FLUXOUT ------------------------------------------------------
@dataclass
class EbcsFluxout(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EBCS/FLUXOUT` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/FLUXOUT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EBCS/GRADP0 ------------------------------------------------------
@dataclass
class EbcsGradp0(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EBCS/GRADP0` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/GRADP0"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /EBCS/INIP ------------------------------------------------------
@dataclass
class EbcsInip(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EBCS/INIP` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/INIP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
