#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MAT/LAW0                   /MAT/LAW1                   /MAT/LAW2 (PLAS_JOHNS)
# /MAT/PLAS_ZERIL             /MAT/LAW3                   /MAT/LAW4
# /MAT/LAW5                   /MAT/LAW6                   /MAT/K-EPS
#

# --- /MAT/LAW0 ------------------------------------------------------
@dataclass
class MatLaw0(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW0` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW0"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW1 ------------------------------------------------------
@dataclass
class MatLaw1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW1` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- MATPLASJOHNS ----------------------------------------------------------------------------
@dataclass
class MatPlasJohns(Keyword):
    mat_title: str
    rho_i: float
    E: float
    nu: float
    iflag: Literal[0, 1]
    mat_id: int = 1
    unit_id: int = 1
    eps_max_p: float = 1e30
    sigma_max_0: float = 1e30
    # iflag = 0
    a: float = float("nan")
    b: float = float("nan")
    n: float = 1.0
    # iflag = 1
    sigma_y: float = float("nan")
    UTS: float = float("nan")
    eps_uts: float = float("nan")

    @property
    def keyword(self):
        return f"/MAT/PLAS_JOHNS/{self.mat_id}/{self.unit_id}"

    @property
    def structure(self):
        structure = [
            StringField("mat_title", 1, 10),
            FloatField("rho_i", 1),
            [FloatField("E", 1), FloatField("nu", 3), IntField("iflag", 5)],
        ]

        if self.iflag == 0:
            structure.extend(
                [
                    [
                        FloatField("a", 1),
                        FloatField("b", 3),
                        FloatField("n", 5),
                        FloatField("eps_max_p", 7),
                        FloatField("sigma_max_0", 9),
                    ]
                ]
            )
        elif self.iflag == 1:
            # TODO: Another line must be added. See documentation.
            structure.extend(
                [
                    [
                        FloatField("sigma_y", 1),
                        FloatField("UTS", 3),
                        FloatField("eps_uts", 5),
                        FloatField("eps_max_p", 7),
                        FloatField("sigma_max_0", 9),
                    ]
                ]
            )
        else:
            raise RuntimeError(
                f"Value of `iflag` must be either 0 or 1 not {self.iflag}"
            )

        return structure


# --- /MAT/PLAS_ZERIL ------------------------------------------------------
@dataclass
class MatPlasZeril(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/PLAS_ZERIL` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/PLAS_ZERIL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW3 ------------------------------------------------------
@dataclass
class MatLaw3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW3` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW4 ------------------------------------------------------
@dataclass
class MatLaw4(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW4` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW4"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW5 ------------------------------------------------------
@dataclass
class MatLaw5(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW5` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW5"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW6 ------------------------------------------------------
@dataclass
class MatLaw6(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/LAW6` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW6"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/K-EPS ------------------------------------------------------
@dataclass
class MatKEps(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/MAT/K-EPS` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/K-EPS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
