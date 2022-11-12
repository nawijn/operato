#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Sequence

from numpy.typing import NDArray

from ..common import (
    FloatField,
    IntField,
    Keyword,
    KeywordStructureType,
    StringField,
    has_all_nones,
    has_shape,
    is_exclusive,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /THPART/GRSPRI              /THPART/GRTRUS              /TITLE
#                             /TRANSFORM/MATRIX           /TRANSFORM/POSITION
# /TRANSFORM/ROT              /TRANSFORM/SCA              /TRANSFORM/SYM
#

# --- /THPART/GRSPRI ------------------------------------------------------
@dataclass
class ThpartGrspri(Keyword):
    """Defines a time-history part for spring groups."""

    th_part_id: int
    th_part_title: str
    grelem_id: int

    @property
    def keyword(self):
        return f"/THPART/GRSPRI/{self.th_part_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("th_part_title", 1, 10),
            IntField("grelem_id", 1),
        ]

        return structure


# --- /THPART/GRTRUS ------------------------------------------------------
@dataclass
class ThpartGrtrus(Keyword):
    """Defines a time-history part for truss groups."""

    th_part_id: int
    th_part_title: str
    grelem_id: int

    @property
    def keyword(self):
        return f"/THPART/GRTRUS/{self.th_part_title}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("th_part_title", 1, 10),
            IntField("grelem_id", 1),
        ]

        return structure


# --- /TITLE ------------------------------------------------------
@dataclass
class Title(Keyword):
    """Describes the title."""

    title: str

    @property
    def keyword(self):
        return "/TITLE"

    @property
    def pre_conditions(self):
        return [(not self.title.startswith("/"), "Titles cannot start with a `/`.")]

    @property
    def structure(self):
        structure: KeywordStructureType = [StringField("title", 1, 10)]

        return structure


# --- /TRANSFORM/MATRIX ------------------------------------------------------
@dataclass
class TransformMatrix(Keyword):
    transform_id: int
    transform_title: str
    M: list[list] | NDArray
    T: Sequence[float] | NDArray
    grnd_id: int | None = None
    sub_id: int | None = None
    unit_id: int | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.tx = None
        self.ty = None
        self.tz = None
        self.m11 = None
        self.m12 = None
        self.m13 = None
        self.m21 = None
        self.m22 = None
        self.m23 = None
        self.m31 = None
        self.m32 = None
        self.m33 = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/TRANSFORM/MATRIX/{self.transform_id}/{self.unit_id}"
        else:
            return f"/TRANSFORM/MATRIX/{self.transform_id}"

    @property
    def pre_conditions(self):
        return [
            (
                is_exclusive(self.grnd_id, self.sub_id),
                "Either `grnd_id` or `sub_id` must be provided. Not both.",
            ),
            (has_shape(self.T, (3, 1)), "Shape of `T` must be (3, 1)."),
            (has_shape(self.M, (3, 3)), "Shape of `M` must be (3, 3)."),
        ]

    @property
    def structure(self):

        self.m11, self.m12, self.m13 = self.M[0]
        self.m21, self.m22, self.m23 = self.M[1]
        self.m31, self.m32, self.m33 = self.M[2]
        self.tx, self.ty, self.tz = self.T

        structure: KeywordStructureType = [
            StringField("transform_title", 1, 10),
            [
                IntField("grnd_id", 1),
                FloatField("m11", 2),
                FloatField("m12", 4),
                FloatField("m13", 6),
                FloatField("tx", 8),
                IntField("sub_id", 10),
            ],
            [
                FloatField("m21", 2),
                FloatField("m22", 4),
                FloatField("m23", 6),
                FloatField("ty", 8),
            ],
            [
                FloatField("m31", 2),
                FloatField("m32", 4),
                FloatField("m33", 6),
                FloatField("ty", 8),
            ],
        ]

        return structure


# --- /TRANSFORM/POSITION ------------------------------------------------------
@dataclass
class TransformPosition(Keyword):
    transform_id: int
    transform_title: str
    grnd_id: int | None = None
    sub_id: int | None = None
    node_id_1: int | None = None
    node_id_2: int | None = None
    node_id_3: int | None = None
    node_id_4: int | None = None
    node_id_5: int | None = None
    node_id_6: int | None = None
    point_1: list[float] | NDArray | None = None
    point_2: list[float] | NDArray | None = None
    point_3: list[float] | NDArray | None = None
    point_4: list[float] | NDArray | None = None
    point_5: list[float] | NDArray | None = None
    point_6: list[float] | NDArray | None = None
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/TRANSFORM/POSITION/{self.transform_id}/{self.unit_id}"
        else:
            return f"/TRANSFORM/POSITION/{self.transform_id}"

    @property
    def pre_conditions(self):
        node_ids = (
            self.node_id_1,
            self.node_id_2,
            self.node_id_3,
            self.node_id_4,
            self.node_id_5,
            self.node_id_6,
        )

        points = (
            self.point_1,
            self.point_2,
            self.point_3,
            self.point_4,
            self.point_5,
            self.point_6,
        )

        return [
            (
                is_exclusive(self.grnd_id, self.sub_id),
                "Either `grnd_id` or `sub_id` must be provided, not both.",
            ),
            (
                not (has_all_nones(node_ids) and has_all_nones(points)),
                "No node ids or points provided; keyword definition is incomplete.",
            ),
            (
                is_exclusive(node_ids, points),
                "Either node ids or points must be provided, not both.",
            ),
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("transform_title", 1, 10),
            [
                IntField("grnd_id", 1),
                IntField("node_id_1", 2),
                IntField("node_id_2", 3),
                IntField("node_id_3", 4),
                IntField("node_id_4", 5),
                IntField("node_id_5", 6),
                IntField("node_id_6", 7),
                IntField("sub_id", 10),
            ],
        ]

        # We only need to check if one point is defined, the condition that all
        # other points are defined is checked in the `pre_conditions` method.
        if self.point_1:
            for i in range(6):
                fields = []
                for j, c in enumerate(("x", "y", "z")):
                    # Generate the name of the attribute
                    attr = f"{c}_point_{i+1}"

                    # Get point for which we want to expande the coordinates
                    point_i = getattr(self, f"point_{i+1}")

                    # Create the attribute ("x", "y" or "z") and set is corresponding value
                    setattr(self, attr, point_i[j])

                    # Calculate the position on the line in the keyword text representaion.
                    pos = 2 * (1 + j)

                    # Create a `FloatField` for this attribute
                    fields.append(FloatField(attr, pos))

                # Add the fields for this point to the `structure` list.
                structure.append(fields)

                # Prepare for next point.
                fields = []

        return structure


# --- /TRANSFORM/ROT ------------------------------------------------------
@dataclass
class TransformRot(Keyword):
    transform_id: int
    transform_title: str
    grnd_id: int | None = None
    sub_id: int | None = None
    node_id_1: int | None = None
    node_id_2: int | None = None
    point_1: list[float] | NDArray | None = None
    point_2: list[float] | NDArray | None = None
    angle: float = 0.0
    unit_id: int | None = None

    def __post_init__(self) -> None:
        super().__post_init__()

        self.x_point_1 = None
        self.y_point_1 = None
        self.z_point_1 = None
        self.x_point_2 = None
        self.y_point_2 = None
        self.z_point_2 = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/TRANSFORM/ROT/{self.transform_id}/{self.unit_id}"
        else:
            return f"/TRANSFORM/ROT/{self.transform_id}"

    @property
    def pre_conditions(self):

        node_ids = [self.node_id_1, self.node_id_2]
        points = [self.point_1, self.point_2]

        conditions = [
            (
                is_exclusive(self.grnd_id, self.sub_id),
                "Either `grnd_id` or `sub_id` must be provided, not both.",
            ),
            (
                not (has_all_nones(node_ids) and has_all_nones(points)),
                "No node ids or points provided; keyword definition is incomplete.",
            ),
            (
                is_exclusive(node_ids, points),
                "Either node ids or points must be provided, not both.",
            ),
        ]

        if self.point_1:
            conditions.extend(
                [
                    (
                        has_shape(self.point_1, (3, 1)),
                        "Expected 3 coordinates for `point_1`",
                    ),
                    (
                        has_shape(self.point_2, (3, 1)),
                        "Expected 3 coordinates for `point_2`",
                    ),
                ]
            )

        return conditions

    @property
    def structure(self):
        if self.point_1:
            self.x_point_1, self.y_point_1, self.z_point_1 = self.point_1

        if self.point_2:
            self.x_point_2, self.y_point_2, self.z_point_2 = self.point_2

        structure: KeywordStructureType = [
            StringField("transform_title", 1, 10),
            [
                IntField("grnd_id", 1),
                FloatField("x_point_1", 2),
                FloatField("y_point_1", 4),
                FloatField("z_point_1", 6),
                IntField("node_id_1", 8),
                IntField("node_id_2", 9),
                IntField("sub_id", 10),
            ],
            [
                FloatField("x_point_2", 2),
                FloatField("y_point_2", 4),
                FloatField("z_point_2", 6),
                FloatField("angle", 8),
            ],
        ]

        return structure


# --- /TRANSFORM/SCA ------------------------------------------------------
@dataclass
class TransformSca(Keyword):
    transform_id: int
    transform_title: str
    grnd_id: int | None = None
    fscale_x: float = 0.0
    fscale_y: float = 0.0
    fscale_z: float = 0.0
    node_id_c: int | None = None
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/TRANSFORM/SCA/{self.transform_id}/{self.unit_id}"
        else:
            return f"/TRANSFORM/SCA/{self.transform_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("transform_title", 1, 10),
            [
                IntField("grnd_id", 1),
                FloatField("fscale_x", 2),
                FloatField("fscale_y", 4),
                FloatField("fscale_z", 6),
                IntField("node_id_c", 8),
            ],
        ]

        return structure


# --- /TRANSFORM/SYM ------------------------------------------------------
@dataclass
class TransformSym(Keyword):
    transform_id: int
    transform_title: str
    grnd_id: int | None = None
    node_id_1: int | None = None
    node_id_2: int | None = None
    point_1: list[float] | NDArray | None = None
    point_2: list[float] | NDArray | None = None
    unit_id: int | None = None

    def __post_init__(self) -> None:
        super().__post_init__()

        self.x_point_1 = None
        self.y_point_1 = None
        self.z_point_1 = None
        self.x_point_2 = None
        self.y_point_2 = None
        self.z_point_2 = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/TRANSFORM/SYM/{self.transform_id}/{self.unit_id}"
        else:
            return f"/TRANSFORM/SYM/{self.transform_id}"

    @property
    def pre_conditions(self):

        node_ids = [self.node_id_1, self.node_id_2]
        points = [self.point_1, self.point_2]

        conditions = [
            (
                not (has_all_nones(node_ids) and has_all_nones(points)),
                "No node ids or points provided; keyword definition is incomplete.",
            ),
            (
                is_exclusive(node_ids, points),
                "Either node ids or points must be provided, not both.",
            ),
        ]

        if self.point_1:
            conditions.extend(
                [
                    (
                        has_shape(self.point_1, (3, 1)),
                        "Expected 3 coordinates for `point_1`",
                    ),
                    (
                        has_shape(self.point_2, (3, 1)),
                        "Expected 3 coordinates for `point_2`",
                    ),
                ]
            )

        return conditions

    @property
    def structure(self):
        if self.point_1:
            self.x_point_1, self.y_point_1, self.z_point_1 = self.point_1

        if self.point_2:
            self.x_point_2, self.y_point_2, self.z_point_2 = self.point_2

        structure: KeywordStructureType = [
            StringField("transform_title", 1, 10),
            [
                IntField("grnd_id", 1),
                FloatField("x_point_1", 2),
                FloatField("y_point_1", 4),
                FloatField("z_point_1", 6),
                IntField("node_id_1", 8),
                IntField("node_id_2", 9),
            ],
            [
                FloatField("x_point_2", 2),
                FloatField("y_point_2", 4),
                FloatField("z_point_2", 6),
            ],
        ]

        return structure
