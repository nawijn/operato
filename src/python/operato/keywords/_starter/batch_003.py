#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Literal, Sequence, Tuple, get_args

from numpy.typing import NDArray

from ...constants import VALID_LENGTH_LITERALS, VALID_MASS_LITERALS, VALID_TIME_LITERALS
from ..common import (
    ArrayOfAtomicFields,
    FloatField,
    IntField,
    Keyword,
    KeywordPreconditionsType,
    KeywordStructureType,
    MultiLineArrayOfAtomicFields,
    StringField,
    TextAlignment,
    VLSequenceOfAtomicField,
    check_if_all_values_are_present,
    get_literal_values,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /BEGIN                      /BEM/DAA                    /BEM/FLOW
# Note: /BOX does not exist   /BOX/BOX                    /BRICK
# /BRIC20                     /CHECK/RFILE/OFF            /CLOAD
#

# --- /BEGIN ----------------------------------------------------------------------------------
@dataclass
class Begin(Keyword):
    # All the variables referenced in the block
    runname: str
    invers: Literal[
        90, 100, 110, 120, 130, 140, 2017, 2018, 2019, 2020, 2021, 2022
    ] = 2022
    input_mass_unit: VALID_MASS_LITERALS = "kg"
    input_length_unit: VALID_LENGTH_LITERALS = "m"
    input_time_unit: VALID_TIME_LITERALS = "s"
    work_mass_unit: VALID_MASS_LITERALS = "kg"
    work_length_unit: VALID_LENGTH_LITERALS = "m"
    work_time_unit: VALID_TIME_LITERALS = "s"

    @property
    def keyword(self):
        return "/BEGIN"

    @property
    def pre_conditions(self):
        return [
            (len(self.runname) <= 80, "`runname` too long (>80)"),
            (
                self.invers in get_literal_values(self, "invers"),
                "Invalid version (see documentation for valid versions).",
            ),
            (
                self.input_mass_unit in get_args(VALID_MASS_LITERALS),
                f"Invalid input mass unit `{self.input_mass_unit}`.",
            ),
            (
                self.input_length_unit in get_args(VALID_LENGTH_LITERALS),
                f"Invalid input length unit `{self.input_length_unit}`.",
            ),
            (
                self.input_time_unit in get_args(VALID_TIME_LITERALS),
                f"Invalid input time unit `{self.input_time_unit}`.",
            ),
            (
                self.work_mass_unit in get_args(VALID_MASS_LITERALS),
                f"Invalid work mass unit `{self.work_mass_unit}`.",
            ),
            (
                self.work_length_unit in get_args(VALID_LENGTH_LITERALS),
                f"Invalid work length unit `{self.work_length_unit}`.",
            ),
            (
                self.work_time_unit in get_args(VALID_TIME_LITERALS),
                f"Invalid work time unit `{self.work_time_unit}`.",
            ),
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("runname", 1, 8),
            IntField("invers", 1),
            [
                StringField("input_mass_unit", 1, 2),
                StringField("input_length_unit", 3, 2),
                StringField("input_time_unit", 5, 2),
            ],
            [
                StringField("work_mass_unit", 1, 2),
                StringField("work_length_unit", 3, 2),
                StringField("work_time_unit", 5, 2),
            ],
        ]

        return structure


# --- /BEM/DAA ------------------------------------------------------
@dataclass
class BemDaa(Keyword):
    daa_id: int
    daa_title: str
    surf_id: int
    grav_id: int
    rho: float
    C: float
    x_s: float
    y_s: float
    z_s: float
    p_min: float = 1.0e-30
    i_form: Literal[1, 2] = 1
    i_pri: Literal[1, 2] = 1
    i_pres: Literal[1, 2] = 1
    k_form: Literal[1, 2] = 1
    freesurf: Literal[1, 2] = 1
    afterflow: Literal[1, 2] = 2
    integr: Literal[1, 2] = 2
    p_m: float | None = None
    theta: float | None = None
    a: float | None = None
    a_theta: float | None = None
    fct_id_p: int | None = None
    fscale_p: float | None = None
    x_c: float | None = None
    y_c: float | None = None
    z_c: float | None = None
    x_a: float | None = None
    y_a: float | None = None
    z_a: float | None = None
    dir_x: float | None = None
    dir_y: float | None = None
    dir_z: float | None = None
    unit_id: int | None = None

    @property
    def keyword(self):
        if not self.unit_id:
            return f"/BEM/DAA/{self.daa_id}"
        else:
            return f"/BEM/DAA/{self.daa_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        conditions = []

        for attr in (
            "i_form",
            "i_pri",
            "i_pres",
            "k_form",
            "freesurf",
            "afterflow",
            "integr",
        ):
            conditions.append(
                (
                    getattr(self, attr) in get_literal_values(self, attr),
                    f"Invalid value for `{attr}`. See documentation for details.",
                )
            )

        if self.i_pres == 1:
            is_complete, not_defined = check_if_all_values_are_present(
                self, ("p_m", "theta", "a", "a_theta")
            )

            conditions.append(
                (
                    is_complete,
                    f"Mandatory parameter(s) `{not_defined}` is/are not defined (i_pres = 1)",
                )
            )

        if self.i_pres == 2:
            is_complete, not_defined = check_if_all_values_are_present(
                self, ("fct_id_p", "fscale_p", "x_c", "y_c", "z_c")
            )

            conditions.append(
                (
                    is_complete,
                    f"Mandatory parameter(s) `{not_defined}` is/are not defined (i_pres = 2)",
                )
            )

        if self.grav_id > 0 or self.freesurf == 2:
            is_complete, not_defined = check_if_all_values_are_present(
                self, ("x_a", "y_a", "z_a", "dir_x", "dir_y", "dir_z")
            )

            conditions.append(
                (
                    is_complete,
                    f"Mandatory parameter(s) `{not_defined}` is/are not defined (i_pres = 2)",
                )
            )

        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("daa_title", 1, 10),
            [IntField("surf_id", 1), IntField("grav_id", 2)],
            [
                FloatField("rho", 1),
                FloatField("C", 3),
                FloatField("p_min", 5),
            ],
            [
                FloatField("x_s", 1),
                FloatField("y_s", 3),
                FloatField("z_s", 5),
            ],
            [
                IntField("i_form", 1),
                IntField("i_pri", 2),
                IntField("i_pres", 3),
                IntField("k_form", 6),
                IntField("freesurf", 7),
                IntField("afterflow", 8),
                IntField("integr", 9),
            ],
        ]

        if self.i_pres == 1:
            structure.append(
                [
                    FloatField("p_m", 1),
                    FloatField("theta", 3),
                    FloatField("a", 5),
                    FloatField("a_theta", 7),
                ]
            )
        elif self.i_pres == 2:
            structure.extend(
                [
                    [IntField("fct_id_p", 1), FloatField("fscale_p", 3)],
                    [
                        FloatField("x_c", 1),
                        FloatField("y_c", 3),
                        FloatField("z_c", 5),
                    ],
                ]
            )

        if self.grav_id > 0 or self.freesurf == 2:
            structure.extend(
                [
                    [
                        FloatField("x_a", 1),
                        FloatField("y_a", 3),
                        FloatField("z_a", 5),
                    ],
                    [
                        FloatField("dir_x", 1),
                        FloatField("dir_y", 3),
                        FloatField("dir_z", 5),
                    ],
                ]
            )

        return structure


# --- /BEM/FLOW ------------------------------------------------------
@dataclass
class BemFlow(Keyword):
    """Describes the incompressible fluid flow by boundary elements method."""

    flow_id: int
    flow_title: str
    surf_id_ex: int
    n_io: int
    fct_id_fsp: int
    grn_id_aux: int
    i_test: int
    rho: float
    i_vinf: int
    i_pri: int
    fct_id_v: int
    dir_x: float
    dir_y: float
    dir_z: float
    i_inside: Literal[1, 2] = 1
    fscale_fsp: float = 1.0
    ascale_fsp: float = 1.0
    tole: float = 1e-5
    # If `n_io > 0` insert `n_io` times
    surf_id_io: List[int] | None = None
    fct_id_nv: List[int] | None = None
    fct_id_p: List[int] | None = None
    fscale_nv: List[float] | None = None
    fscale_p: List[float] | None = None
    ascale_t: List[float] | None = None
    # Formulation flags
    i_form: Literal[1, 2] = 1
    dt_flow: float = 0.0
    fscale_v: float = 1.0
    ascale_v: float = 1.0
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/BEM/FLOW/{self.flow_id}/{self.unit_id}"
        else:
            return f"/BEM/FLOW/{self.flow_id}"

    @property
    def pre_conditions(self):
        conditions: KeywordPreconditionsType = []

        for attr in ("i_inside", "i_form"):
            conditions.append(
                (
                    getattr(self, attr) in get_literal_values(self, attr),
                    f"Invalid value for `{attr}`. See documentation for details.",
                )
            )

        if self.n_io > 0:
            for attr in (
                "surf_id_io",
                "fct_id_nv",
                "fct_id_p",
                "fscale_nv",
                "fscale_p",
                "ascale_t",
            ):
                o = getattr(self, attr)
                conditions.append(
                    (isinstance(o, Sequence), f"Attribute `{attr}` must be a sequence")
                )

                if isinstance(o, Sequence):
                    conditions.append(
                        (
                            len(o) == self.n_io,
                            (
                                f"Invalid number of entries in `{attr}`. "
                                "See documentation for details."
                            ),
                        )
                    )

        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("flow_title", 1, 10),
            [
                IntField("surf_id_ex", 1),
                IntField("n_io", 2),
                IntField("i_inside", 3),
                IntField("fct_id_fsp", 4),
                FloatField("fscale_fsp", 5),
                FloatField("ascale_fsp", 7),
            ],
            [
                IntField("grn_id_aux", 1),
                IntField("i_test", 2),
                FloatField("tole", 3),
            ],
            [FloatField("rho", 1), IntField("i_vinf", 3)],
        ]

        if self.n_io > 0:
            structure.append(
                ArrayOfAtomicFields(
                    [
                        IntField("surf_id_io", 1),
                        IntField("fct_id_nv", 2),
                        IntField("fct_id_p", 3),
                        FloatField("fscale_nv", 5),
                        FloatField("fscale_p", 7),
                        FloatField("ascale_t", 9),
                    ]
                )
            )

        structure.extend(
            [
                [
                    IntField("i_form", 1),
                    IntField("i_pri", 2),
                    FloatField("dt_flow", 3),
                ],
                [
                    IntField("fct_id_v", 1),
                    FloatField("fscale_v", 2),
                    FloatField("ascale_v", 4),
                ],
                [
                    FloatField("dir_x", 1),
                    FloatField("dir_y", 3),
                    FloatField("dir_z", 5),
                ],
            ]
        )

        return structure


# --- /BOX/BOX ------------------------------------------------------
@dataclass
class BoxBox(Keyword):
    """Describes the box as a result of the combination of a predefined list of boxes."""

    box_id: int
    box_title: str
    box_ids: List[int]

    @property
    def keyword(self):
        return f"/BOX/BOX/{self.box_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("box_title", 1, 10),
            VLSequenceOfAtomicField(IntField("box_ids", 1)),
        ]

        return structure


# --- /BRICK ------------------------------------------------------
@dataclass
class Brick(Keyword):
    """Defines a hexahedral solid element or thick shell element with 8 nodes.
    The element type and formulation are defined on the /PROP card.
    """

    part_id: int
    brick_ids: List[int] | NDArray
    node_ids: List[Tuple[int, ...]] | NDArray

    @property
    def keyword(self):
        return f"/BRICK/{self.part_id}"

    @property
    def pre_conditions(self):

        return [
            (
                len(self.brick_ids) > 0,
                "Pre-condition `len(brick_ids) > 0` is violated.",
            ),
            (
                len(self.node_ids) > 0,
                "Pre-condition `len(node_ids) > 0` is violated.",
            ),
            (
                len(self.brick_ids) == len(self.node_ids),
                "Pre-condition `len(brick_ids) == len(node_ids)` is violated.",
            ),
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            ArrayOfAtomicFields(
                [
                    IntField("brick_ids", 1),
                    IntField("node_ids:ID_1|0", 2),
                    IntField("node_ids:ID_2|1", 3),
                    IntField("node_ids:ID_3|2", 4),
                    IntField("node_ids:ID_4|3", 5),
                    IntField("node_ids:ID_5|4", 6),
                    IntField("node_ids:ID_6|5", 7),
                    IntField("node_ids:ID_7|6", 8),
                    IntField("node_ids:ID_8|7", 9),
                ]
            )
        ]

        return structure


# --- /BRIC20 ------------------------------------------------------
@dataclass
class Bric20(Keyword):
    """Describes 3D solid elements (20 node brick elements). This quadratic
    element should be used with the property /PROP/SOLID.

    """

    part_id: int
    brick_ids: List[int] | NDArray
    node_ids: List[Tuple[int, ...]] | NDArray

    @property
    def keyword(self):
        return f"/BRIC20/{self.part_id}"

    @property
    def pre_conditions(self):

        return [
            (
                len(self.brick_ids) > 0,
                "Pre-condition `len(brick_ids) > 0` is violated.",
            ),
            (
                len(self.node_ids) > 0,
                "Pre-condition `len(node_ids) > 0` is violated.",
            ),
            (
                len(self.brick_ids) == len(self.node_ids),
                "Pre-condition `len(brick_ids) == len(node_ids)` is violated.",
            ),
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            MultiLineArrayOfAtomicFields(
                [
                    ArrayOfAtomicFields(
                        [
                            IntField("brick_ids", 1),
                            IntField("node_ids:ID_1|0", 2),
                            IntField("node_ids:ID_2|1", 3),
                            IntField("node_ids:ID_3|2", 4),
                            IntField("node_ids:ID_4|3", 5),
                            IntField("node_ids:ID_5|4", 6),
                            IntField("node_ids:ID_6|5", 7),
                            IntField("node_ids:ID_7|6", 8),
                            IntField("node_ids:ID_8|7", 9),
                        ]
                    ),
                    ArrayOfAtomicFields(
                        [
                            IntField("node_ids:ID_9|8", 1),
                            IntField("node_ids:ID_10|9", 2),
                            IntField("node_ids:ID_11|10", 3),
                            IntField("node_ids:ID_12|11", 4),
                            IntField("node_ids:ID_13|12", 5),
                            IntField("node_ids:ID_14|13", 6),
                            IntField("node_ids:ID_15|14", 7),
                            IntField("node_ids:ID_16|15", 8),
                        ]
                    ),
                    ArrayOfAtomicFields(
                        [
                            IntField("node_ids:ID_17|16", 1),
                            IntField("node_ids:ID_18|17", 2),
                            IntField("node_ids:ID_19|18", 3),
                            IntField("node_ids:ID_20|19", 4),
                        ]
                    ),
                ]
            )
        ]

        return structure


# --- /CHECK/RFILE/OFF ------------------------------------------------------
@dataclass
class CheckRfileOff(Keyword):
    @property
    def keyword(self):
        return "/CHECK/RFILE/OFF"


# --- /CLOAD ------------------------------------------------------
@dataclass
class Cload(Keyword):
    cload_id: int
    cload_title: str
    fct_id_t: int
    dir: Literal[
        "X",
        "Y",
        "Z",
        "XY",
        "XZ",
        "YZ",
        "XYZ",
        "XX",
        "YY",
        "ZZ",
        "XXYY",
        "XXZZ",
        "YYZZ",
        "XXYYZZ",
    ]
    skew_id: int
    sens_id: int
    grnd_id: int
    unit_id: int | None = None
    a_scale_x: float = 1.0
    f_scale_y: float = 1.0

    @property
    def keyword(self):
        if self.unit_id is None:
            return f"/CLOAD/{self.cload_id}"
        else:
            return f"/CLOAD/{self.cload_id}/unit_id"

    @property
    def pre_conditions(self):
        return [
            (
                self.dir in get_literal_values(self, "dir"),
                f"Invalid `dir` specifier -> {self.dir}",
            )
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("cload_title", 1, 10),
            [
                IntField("fct_id_t", 1),
                StringField("dir", 2, 1, alignment=TextAlignment.CENTER),
                IntField("skew_id", 3),
                IntField("sens_id", 4),
                IntField("grnd_id", 5),
                FloatField("a_scale_x", 7),
                FloatField("f_scale_y", 9),
            ],
        ]

        return structure
