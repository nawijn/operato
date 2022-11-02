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
    """Describes a planar detonation wave."""

    detp_id: int
    p_id: int
    n_id: int
    t_det: float = 0.0
    mat_id: int = 0
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/DFS/DETPLAN/NODE/{self.detp_id}/{self.unit_id}"
        else:
            return f"/DFS/DETPLAN/NODE/{self.detp_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            [FloatField("t_det", 7), IntField("mat_id", 9), IntField("p_id", 10)],
            IntField("n_id", 10),
        ]

        return structure


# --- /DFS/DETPOINT ------------------------------------------------------
@dataclass
class DfsDetpoint(Keyword):
    """Locates the detonation point and set lighting time for an explosive
    material law."""

    detpoint_id: int
    x_det: float = 0.0
    y_det: float = 0.0
    z_det: float = 0.0
    t_det: float = 0.0
    mat_id: float = 0

    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/DFS/DETPOINT/{self.detpoint_id}/{self.unit_id}"
        else:
            return f"/DFS/DETPOINT/{self.detpoint_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            [
                FloatField("x_det", 1),
                FloatField("y_det", 3),
                FloatField("z_det", 5),
                FloatField("t_det", 7),
                IntField("mat_id", 9),
            ]
        ]

        return structure


# --- /DFS/DETPOINT/NODE ------------------------------------------------------
@dataclass
class DfsDetpointNode(Keyword):
    detpoint_id: int
    t_det: float
    node_id: int
    mat_id: int = 0
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/DFS/DETPOINT/NODE/{self.detpoint_id}/{self.unit_id}"
        else:
            return f"/DFS/DETPOINT/NODE/{self.detpoint_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            [
                FloatField("t_det", 7),
                IntField("mat_id", 9),
                IntField("node_id", 10),
            ]
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
        structure = []

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
        structure = []

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
        structure = []

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
        structure = []

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
        structure = []

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
        structure = []

        return structure
