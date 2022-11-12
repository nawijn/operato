#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal

from numpy.typing import NDArray

from ...constants import VALID_LENGTH_LITERALS, VALID_MASS_LITERALS, VALID_TIME_LITERALS
from ..common import (
    ArrayOfAtomicFields,
    FloatField,
    IntField,
    Keyword,
    KeywordStructureType,
    StringField,
    get_args,
    get_literal_values,
    have_same_length,
    is_exclusive,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /TRANSFORM/TRA              /TRIA                       /TRUSS
# /UNIT                       /UPWIND                     /VISC/PRONY
# /XELEM                      /XREF
#

# --- /TRANSFORM/TRA ------------------------------------------------------
@dataclass
class TransformTra(Keyword):
    """Defines a translation for a node group with a defined vector."""

    transform_id: int
    transform_title: str
    grnd_id: int | None = None
    x_translation: float | None = 0.0
    y_translation: float | None = 0.0
    z_translation: float | None = 0.0
    node_id_1: int | None = None
    node_id_2: int | None = None
    sub_id: int | None = None
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/TRANSFORM/TRA/{self.transform_id}/{self.unit_id}"
        else:
            return f"/TRANSFORM/TRA/{self.transform_id}"

    @property
    def pre_conditions(self):
        conditions = [
            (
                is_exclusive(self.grnd_id, self.sub_id),
                "Either `grnd_id` or `sub_id` must be provided, not both.",
            )
        ]

        return conditions

    @property
    def structure(self):

        if self.node_id_1 and self.node_id_2:
            self.x_translation = None
            self.y_translation = None
            self.z_translation = None

        structure: KeywordStructureType = [
            StringField("transform_title", 1, 10),
            [
                IntField("grnd_id", 1),
                FloatField("x_translation", 2),
                FloatField("x_translation", 4),
                FloatField("x_translation", 6),
                IntField("node_id_1", 8),
                IntField("node_id_1", 9),
                IntField("sub_id", 10),
            ],
        ]

        return structure


# --- /TRIA ------------------------------------------------------
@dataclass
class Tria(Keyword):
    """Describes the 2D solid elements based on 3 nodes. TRIA elements must be
    defined in the global YZ plane.
    """

    part_id: int
    tria_ids: list | tuple | NDArray
    node_ids: NDArray

    @property
    def keyword(self):
        return f"/TRIA/{self.part_id}"

    @property
    def pre_conditions(self):

        return [
            (
                have_same_length(self.tria_ids, self.node_ids),
                "Pre-condition `len(tria_ids) == len(node_ids)` is violated.",
            )
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            ArrayOfAtomicFields(
                [
                    IntField("tria_ids", 1),
                    IntField("node_ids:ID_1|0", 2),
                    IntField("node_ids:ID_2|1", 3),
                    IntField("node_ids:ID_3|2", 4),
                ]
            )
        ]

        return structure


# --- /TRUSS ------------------------------------------------------
@dataclass
class Truss(Keyword):
    """Describes one dimension truss elements, which could be used with
    property /PROP/TYPE2 (TRUSS). Truss could only carry axial load (like for
    bar).

    """

    part_id: int
    truss_ids: list | tuple | NDArray
    node_ids: NDArray

    @property
    def keyword(self):
        return f"/TRUSS/{self.part_id}"

    @property
    def pre_conditions(self):

        return [
            (
                have_same_length(self.truss_ids, self.node_ids),
                "Pre-condition `len(truss_ids) == len(node_ids)` is violated.",
            )
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            ArrayOfAtomicFields(
                [
                    IntField("truss_ids", 1),
                    IntField("node_ids:ID_1|0", 2),
                    IntField("node_ids:ID_2|1", 3),
                ]
            )
        ]

        return structure


# --- /UNIT ------------------------------------------------------
@dataclass
class Unit(Keyword):
    """Defines a local unit system for the keywords listed below."""

    unit_title: str
    mass_unit: VALID_MASS_LITERALS
    length_unit: VALID_LENGTH_LITERALS
    time_unit: VALID_TIME_LITERALS
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/UNIT/{self.unit_id}"
        else:
            return "/UNIT"

    @property
    def pre_conditions(self):
        conditions = [
            (
                self.mass_unit in get_args(VALID_MASS_LITERALS),
                f"Invalid input mass unit `{self.mass_unit}`.",
            ),
            (
                self.length_unit in get_args(VALID_LENGTH_LITERALS),
                f"Invalid input length unit `{self.length_unit}`.",
            ),
            (
                self.time_unit in get_args(VALID_TIME_LITERALS),
                f"Invalid input time unit `{self.time_unit}`.",
            ),
        ]

        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("unit_title", 1, 10),
            [
                StringField("mass_unit", 1, 2),
                StringField("length_unit", 3, 2),
                StringField("time_unit", 5, 2),
            ],
        ]

        return structure


# --- /UPWIND ------------------------------------------------------
@dataclass
class Upwind(Keyword):
    """Describes the upwind coefficient."""

    eta_1: float = 1.0
    eta_2: float = 1.0
    eta_3: float = 1.0

    @property
    def keyword(self):
        return "/UPWIND"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            [
                FloatField("eta_1", 1),
                FloatField("eta_2", 3),
                FloatField("eta_3", 5),
            ]
        ]

        return structure


# --- /VISC/PRONY ------------------------------------------------------
@dataclass
class ViscProny(Keyword):
    """This is an isotropic visco-elastic Maxwell model that can be used to
    add visco-elasticity to certain shell and solid element material models.
    The visco-elasticity is input using a Prony series."""

    mat_id: int
    M: int = 0
    K_nu: float = 0.0
    i_tab: Literal[0, 1, 2] = 0
    # i_tab > 0
    i_shape: Literal[0, 1] = 0
    # i_tab == 0
    G_i: float | None = None
    beta_i: float | None = None
    K_i: float | None = None
    beta_ki: float | None = None
    # i_tab == 1
    i_func_g: int | None = None
    i_func_k: int | None = None
    xg_scale: float = 1.0
    yg_scale: float = 1.0
    xk_scale: float = 1.0
    yk_scale: float = 1.0
    # i_tab == 2
    i_func_gs: int | None = None
    i_func_gl: int | None = None
    i_func_ks: int | None = None
    i_func_kl: int | None = None
    xgs_scale: float = 1.0
    ygs_scale: float = 1.0
    xgl_scale: float = 1.0
    ygl_scale: float = 1.0
    xks_scale: float = 1.0
    yks_scale: float = 1.0
    xkl_scale: float = 1.0
    ykl_scale: float = 1.0

    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/VISC/PRONY/{self.mat_id}/{self.unit_id}"
        else:
            return f"/VISC/PRONY/{self.mat_id}"

    @property
    def pre_conditions(self):
        conditions = []

        for attr in ("i_tab", "i_shape"):
            conditions.append(
                (
                    getattr(self, attr) in get_literal_values(self, attr),
                    f"Invalid value for `{attr}`. See documentation for details.",
                )
            )

        return []

    @property
    def structure(self):
        structure: KeywordStructureType = []

        if self.i_tab == 0:
            structure.append(
                [
                    IntField("M", 1),
                    FloatField("K_nu", 3),
                    IntField("i_tab", 5),
                ]
            )

        else:
            structure.append(
                [
                    IntField("M", 1),
                    FloatField("K_nu", 3),
                    IntField("i_tab", 5),
                    IntField("i_shape", 6),
                ]
            )

        if self.i_tab == 0:
            structure.append(
                [
                    FloatField("G_i", 1),
                    FloatField("beta_i", 3),
                    FloatField("K_i", 5),
                    FloatField("beta_ki", 7),
                ]
            )

        elif self.i_tab == 1:
            structure.extend(
                [
                    [
                        IntField("i_func_g", 1),
                        FloatField("xg_scale", 2),
                        FloatField("yg_scale", 4),
                    ],
                    [
                        IntField("i_func_k", 1),
                        FloatField("xk_scale", 2),
                        FloatField("yk_scale", 4),
                    ],
                ]
            )

        elif self.i_tab == 2:
            structure.extend(
                [
                    [
                        IntField("i_func_gs", 1),
                        FloatField("xgs_scale", 2),
                        FloatField("ygs_scale", 4),
                    ],
                    [
                        IntField("i_func_gl", 1),
                        FloatField("xgl_scale", 2),
                        FloatField("ygl_scale", 4),
                    ],
                    [
                        IntField("i_func_ks", 1),
                        FloatField("xks_scale", 2),
                        FloatField("yks_scale", 4),
                    ],
                    [
                        IntField("i_func_kl", 1),
                        FloatField("xkl_scale", 2),
                        FloatField("ykl_scale", 4),
                    ],
                ]
            )

        return structure


# --- /XELEM ------------------------------------------------------
@dataclass
class Xelem(Keyword):
    """Describes the multi-strand element. It could be use with /PROP/TYPE28
    (NSTRAND), and it could be used for belt modelization by taking nodes upon
    the dummy."""

    part_id: int
    elem_id: int
    grnd_id: int
    # TODO: Check if elem_id/grnd_id should actually be arrays instead of single values.

    @property
    def keyword(self):
        return f"/XELEM/{self.part_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            [IntField("elem_id", 1), IntField("grnd_id", 2)]
        ]

        return structure


# --- /XREF ------------------------------------------------------
@dataclass
class Xref(Keyword):
    part_id: int
    xref_title: str
    node_ids: list | tuple | NDArray
    xc_yc_zc: NDArray
    n_itrs: int = 100
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/XREF/{self.part_id}/{self.unit_id}"
        else:
            return f"/XREF/{self.part_id}"

    @property
    def pre_conditions(self):
        # If both `node_ids` and `xc_yc_zc` reference the same array, there is
        # no need to check the length
        return [
            (
                have_same_length(self.node_ids, self.xc_yc_zc),
                "Pre-condition `len(node_ids) == len(xc_yc_zc)` is violated.",
            )
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("xref_title", 1, 10),
            IntField("n_itrs", 1),
            ArrayOfAtomicFields(
                (
                    IntField("node_ids", 1),
                    FloatField("xc_yc_zc:xc|0", 2),
                    FloatField("xc_yc_zc:yc|1", 4),
                    FloatField("xc_yc_zc:xc|2", 6),
                )
            ),
        ]

        return structure
