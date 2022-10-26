#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Literal, Tuple, get_args

from numpy.typing import NDArray

from ...constants import VALID_LENGTH_LITERALS, VALID_MASS_LITERALS, VALID_TIME_LITERALS
from ..common import (
    ArrayOfFields,
    FloatField,
    IntField,
    Keyword,
    StringField,
    TextAlignment,
    get_literal_values,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /BEGIN                      /BEM/DAA                    /BEM/FLOW
# /BOX                        /BOX/BOX                    /BRICK
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
        structure = [
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
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BEM/DAA` is not implemented.")

    @property
    def keyword(self):
        return "/BEM/DAA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /BEM/FLOW ------------------------------------------------------
@dataclass
class BemFlow(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BEM/FLOW` is not implemented.")

    @property
    def keyword(self):
        return "/BEM/FLOW"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /BOX ------------------------------------------------------
@dataclass
class Box(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BOX` is not implemented.")

    @property
    def keyword(self):
        return "/BOX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /BOX/BOX ------------------------------------------------------
@dataclass
class BoxBox(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BOX/BOX` is not implemented.")

    @property
    def keyword(self):
        return "/BOX/BOX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /BRICK ------------------------------------------------------
@dataclass
class Brick(Keyword):
    """Defines a hexahedral solid element or thick shell element with 8 nodes.
    The element type and formulation are defined on the /PROP card.
    """

    part_id: int
    brick_ids: List[int] | NDArray
    node_ids: List[Tuple[int, int, int, int, int, int, int, int]] | NDArray

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
        structure = [
            ArrayOfFields(
                [
                    IntField("brick_ids", 1),
                    IntField("node_ids:0", 2),
                    IntField("node_ids:1", 3),
                    IntField("node_ids:2", 4),
                    IntField("node_ids:3", 5),
                    IntField("node_ids:4", 6),
                    IntField("node_ids:5", 7),
                    IntField("node_ids:6", 8),
                    IntField("node_ids:7", 9),
                ]
            )
        ]

        return structure


# --- /BRIC20 ------------------------------------------------------
@dataclass
class Bric20(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/BRIC20` is not implemented.")

    @property
    def keyword(self):
        return "/BRIC20"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /CHECK/RFILE/OFF ------------------------------------------------------
@dataclass
class CheckRfileOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/CHECK/RFILE/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/CHECK/RFILE/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


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
        structure = [
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
