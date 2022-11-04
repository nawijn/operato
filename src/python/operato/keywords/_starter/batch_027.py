#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal

from ..common import (
    FloatField,
    IntField,
    Keyword,
    KeywordStructureType,
    StringField,
    get_literal_values,
)

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
        structure: KeywordStructureType = []

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
        structure: KeywordStructureType = []

        return structure


# --- MATPLASJOHNS ----------------------------------------------------------------------------
@dataclass
class MatPlasJohns(Keyword):
    """This law represents an isotropic elasto-plastic material using the
    Johnson-Cook material model.  This model expresses material stress as a
    function of strain, strain rate and temperature. A built-in failure
    criterion based on the maximum plastic strain is available.

    """

    mat_id: int
    mat_title: str
    rho_i: float
    E: float
    nu: float
    i_flag: Literal[0, 1] = 0
    # iflag = 0
    a: float | None = None
    b: float | None = None
    n: float = 1.0
    eps_max_p: float = 1e30
    sigma_max_0: float = 1e30
    # iflag = 1
    sigma_y: float | None = None
    UTS: float | None = None
    eps_uts: float | None = None
    # Other
    c: float = 0.0
    eps_rate_0: float | None = None
    icc: Literal[0, 1, 2] = 1
    f_smooth: Literal[0, 1] = 1
    f_cut: float = 1e30
    c_hard: float = 0.0
    m: float = 1.0
    T_melt: float = 1e30
    rho_c_p: float | None = None
    T_r: float = 298
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/MAT/PLAS_JOHNS/{self.mat_id}/{self.unit_id}"
        else:
            return f"/MAT/PLAS_JOHNS/{self.mat_id}"

    @property
    def pre_conditions(self):
        conditions = []

        for attr in ("i_flag", "icc", "f_smooth"):
            conditions.append(
                (
                    getattr(self, attr) in get_literal_values(self, attr),
                    f"Invalid value for `{attr}`. See documentation for details.",
                )
            )

        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("mat_title", 1, 10),
            FloatField("rho_i", 1),
            [FloatField("E", 1), FloatField("nu", 3), IntField("i_flag", 5)],
        ]

        if self.i_flag == 0:
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
        elif self.i_flag == 1:
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

        structure.extend(
            [
                [
                    FloatField("c", 1),
                    FloatField("eps_rate_0", 3),
                    IntField("icc", 5),
                    IntField("f_smooth", 6),
                    FloatField("f_cut", 7),
                    FloatField("c_hard", 9),
                ],
                [
                    FloatField("m", 1),
                    FloatField("T_melt", 3),
                    FloatField("rho_c_p", 5),
                    FloatField("T_r", 7),
                ],
            ]
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
        structure: KeywordStructureType = []

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
        structure: KeywordStructureType = []

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
        structure: KeywordStructureType = []

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
        structure: KeywordStructureType = []

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
        structure: KeywordStructureType = []

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
        structure: KeywordStructureType = []

        return structure
