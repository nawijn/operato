#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /DEFAULT/INTER/TYPE7        /DEFAULT/INTER/TYPE11       /DEFAULT/INTER/TYPE19       
# /DEFAULT/INTER/TYPE24       /DEFAULT/INTER/TYPE25       /DFS/DETCORD                
# /DFS/DETLINE                /DFS/DETLINE/NODE           /DFS/DETPLAN                
#

# --- /DEFAULT/INTER/TYPE7 ------------------------------------------------------
@dataclass
class DefaultInterType7(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DEFAULT/INTER/TYPE7` is not implemented.")

    @property
    def keyword(self):
        return "/DEFAULT/INTER/TYPE7"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DEFAULT/INTER/TYPE11 ------------------------------------------------------
@dataclass
class DefaultInterType11(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DEFAULT/INTER/TYPE11` is not implemented.")

    @property
    def keyword(self):
        return "/DEFAULT/INTER/TYPE11"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DEFAULT/INTER/TYPE19 ------------------------------------------------------
@dataclass
class DefaultInterType19(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DEFAULT/INTER/TYPE19` is not implemented.")

    @property
    def keyword(self):
        return "/DEFAULT/INTER/TYPE19"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DEFAULT/INTER/TYPE24 ------------------------------------------------------
@dataclass
class DefaultInterType24(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DEFAULT/INTER/TYPE24` is not implemented.")

    @property
    def keyword(self):
        return "/DEFAULT/INTER/TYPE24"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DEFAULT/INTER/TYPE25 ------------------------------------------------------
@dataclass
class DefaultInterType25(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DEFAULT/INTER/TYPE25` is not implemented.")

    @property
    def keyword(self):
        return "/DEFAULT/INTER/TYPE25"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DFS/DETCORD ------------------------------------------------------
@dataclass
class DfsDetcord(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/DETCORD` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/DETCORD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DFS/DETLINE ------------------------------------------------------
@dataclass
class DfsDetline(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/DETLINE` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/DETLINE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DFS/DETLINE/NODE ------------------------------------------------------
@dataclass
class DfsDetlineNode(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/DETLINE/NODE` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/DETLINE/NODE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /DFS/DETPLAN ------------------------------------------------------
@dataclass
class DfsDetplan(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/DFS/DETPLAN` is not implemented.")

    @property
    def keyword(self):
        return "/DFS/DETPLAN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
