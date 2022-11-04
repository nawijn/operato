#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /STATE/BRICK/STRES/GLOBFULL /STATE/DT                   /STATE/INIMAP1D/Keyword3    
# /STATE/INIMAP2D/Keyword3    /STATE/LSENSOR              /STATE/NODE/BCS             
# /STATE/NODE/TEMP            /STATE/NODE/VEL             /STATE/NO_DEL               
#

# --- /STATE/BRICK/STRES/GLOBFULL ------------------------------------------------------
@dataclass
class StateBrickStresGlobfull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/BRICK/STRES/GLOBFULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/BRICK/STRES/GLOBFULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/DT ------------------------------------------------------
@dataclass
class StateDt(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/DT` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/DT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/INIMAP1D/Keyword3 ------------------------------------------------------
@dataclass
class StateInimap1dKeyword3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/INIMAP1D/Keyword3` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/INIMAP1D/Keyword3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/INIMAP2D/Keyword3 ------------------------------------------------------
@dataclass
class StateInimap2dKeyword3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/INIMAP2D/Keyword3` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/INIMAP2D/Keyword3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/LSENSOR ------------------------------------------------------
@dataclass
class StateLsensor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/LSENSOR` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/LSENSOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/NODE/BCS ------------------------------------------------------
@dataclass
class StateNodeBcs(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/NODE/BCS` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/NODE/BCS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/NODE/TEMP ------------------------------------------------------
@dataclass
class StateNodeTemp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/NODE/TEMP` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/NODE/TEMP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/NODE/VEL ------------------------------------------------------
@dataclass
class StateNodeVel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/NODE/VEL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/NODE/VEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 


# --- /STATE/NO_DEL ------------------------------------------------------
@dataclass
class StateNoDel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/STATE/NO_DEL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/NO_DEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [

        ]

        return structure 
