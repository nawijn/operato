#!/usr/bin/env python3

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from ..common import ArrayOfAtomicFields, FloatField, IntField, Keyword

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MONVOL/GAS                 /MONVOL/LFLUID              /MONVOL/PRES
# /MOVE_FUNCT                 /MPC                        /NBCS
# /NODE                       /NONLOCAL/MAT               /PARAMETER
#

# --- /MONVOL/GAS ------------------------------------------------------
@dataclass
class MonvolGas(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MONVOL/GAS` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/GAS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MONVOL/LFLUID ------------------------------------------------------
@dataclass
class MonvolLfluid(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MONVOL/LFLUID` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/LFLUID"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MONVOL/PRES ------------------------------------------------------
@dataclass
class MonvolPres(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MONVOL/PRES` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/PRES"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MOVE_FUNCT ------------------------------------------------------
@dataclass
class MoveFunct(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MOVE_FUNCT` is not implemented.")

    @property
    def keyword(self):
        return "/MOVE_FUNCT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MPC ------------------------------------------------------
@dataclass
class Mpc(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MPC` is not implemented.")

    @property
    def keyword(self):
        return "/MPC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /NBCS ------------------------------------------------------
@dataclass
class Nbcs(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/NBCS` is not implemented.")

    @property
    def keyword(self):
        return "/NBCS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- NODE ------------------------------------------------------------------------------------
@dataclass
class Node(Keyword):
    unit_id: int
    node_ids: list | tuple | NDArray
    xc_yc_zc: NDArray

    @property
    def keyword(self):
        return f"/NODE/{self.unit_id}"

    @property
    def pre_conditions(self):
        node_ids = self.node_ids
        xc_yc_zc = self.xc_yc_zc

        if isinstance(node_ids, (tuple, list)):
            node_ids = np.array(node_ids)

        return [
            (
                len(node_ids) == len(xc_yc_zc),
                "Pre-condition `len(node_ids) == len(xc_yc_zc)` failed",
            ),
            (
                node_ids.shape == (len(node_ids),),
                "Pre-conditions `node_ids.shape == len(node_ids,)` failed.",
            ),
            (
                xc_yc_zc.shape == (len(xc_yc_zc), 3),
                "Pre-conditions `xc_yc_zc.shape == len(xc_yc_zc, 3)` failed.",
            ),
        ]

    @property
    def structure(self):
        structure = [
            ArrayOfAtomicFields(
                (
                    IntField("node_ids", 1),
                    FloatField("xc_yc_zc:0", 2),
                    FloatField("xc_yc_zc:1", 4),
                    FloatField("xc_yc_zc:2", 6),
                )
            )
        ]

        return structure


# --- /NONLOCAL/MAT ------------------------------------------------------
@dataclass
class NonlocalMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/NONLOCAL/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/NONLOCAL/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PARAMETER ------------------------------------------------------
@dataclass
class Parameter(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PARAMETER` is not implemented.")

    @property
    def keyword(self):
        return "/PARAMETER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
