#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal, List

from ..common import (
    FloatField,
    IntField,
    Keyword,
    KeywordPreconditionsType,
    StringField,
    KeywordStructureType,
    get_literal_values,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /CLUSTER                    /CNODE                      /CONVEC
# /CYL_JOINT                  /DAMP                       /DAMP/INTER
# /DEF_SHELL                  /DEF_SOLID                  /DEFAULT/INTER/TYPE2
#

# --- /CLUSTER ------------------------------------------------------
@dataclass
class Cluster(Keyword):
    """Describes an assembly of brick or spring elements for post-processing
    and failure control.

    """

    cluster_id: int
    cluster_title: str
    group_id: int
    skew_id: int
    i_fail: Literal[0, 1, 2, 3] = 0
    fn_fail: float = 1e30
    fs_fail: float = 1e30
    mt_fail: float = 1e30
    mb_fail: float = 1e30
    a1: float = 1.0
    a2: float = 1.0
    a3: float = 1.0
    a4: float = 1.0
    b1: float = 1.0
    b2: float = 1.0
    b3: float = 1.0
    b4: float = 1.0
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/CLUSTER/{self.cluster_id}/{self.unit_id}"
        else:
            return f"/CLUSTER/{self.cluster_id}"

    @property
    def pre_conditions(self):
        conditions: KeywordPreconditionsType = []

        conditions.append(
            (
                self.i_fail in get_literal_values(self, "i_fail"),
                "Invalid value for `i_fail`. See documentation for details.",
            )
        )

        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("cluster_title", 1, 10),
            [
                IntField("group_id", 1),
                IntField("skew_id", 2),
                IntField("i_fail", 3),
            ],
        ]

        if self.i_fail != 3:
            structure.extend(
                [
                    FloatField("fn_fail", 1),
                    FloatField("fs_fail", 1),
                    FloatField("mt_fail", 1),
                    FloatField("mb_fail", 1),
                ]
            )
        else:
            structure.extend(
                [
                    [
                        FloatField("fn_fail", 1),
                        FloatField("a1", 3),
                        FloatField("b1", 5),
                    ],
                    [
                        FloatField("fs_fail", 1),
                        FloatField("a2", 3),
                        FloatField("b2", 5),
                    ],
                    [
                        FloatField("mt_fail", 1),
                        FloatField("a3", 3),
                        FloatField("b3", 5),
                    ],
                    [
                        FloatField("mb_fail", 1),
                        FloatField("a4", 3),
                        FloatField("b4", 5),
                    ],
                ]
            )

        return structure


# --- /CNODE ------------------------------------------------------
@dataclass
class Cnode(Keyword):
    """Defines the coordinate of common node, which could be merged to the
    nearest selected NODE or CNODE."""

    search_value: float
    cnode_id: int
    x_c: float
    y_c: float
    z_c: float
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/CNODE/{self.search_value}/self.unit_id"
        else:
            return f"/CNODE/{self.search_value}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            [
                IntField("cnode_id", 1),
                FloatField("x_c", 2),
                FloatField("y_c", 4),
                FloatField("z_c", 6),
            ]
        ]

        return structure


# --- /CONVEC ------------------------------------------------------
@dataclass
class Convec(Keyword):
    """Describes the free or forced convective flux."""

    convec_id: int
    convec_flux_title: str
    surf_id_t: int
    fct_id_t: int
    sens_id: int
    t_start: float
    H: float
    ascale_x: float = 1.0
    fscale_y: float = 1.0
    t_stop: float = 1e30
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/CONVEC/{self.convec_id}/{self.unit_id}"
        else:
            return f"/CONVEC/{self.convec_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("convec_flux_title", 1, 10),
            [
                IntField("surf_id_t", 1),
                IntField("fct_id_t", 2),
                IntField("sens_id", 3),
            ],
            [
                FloatField("ascale_x", 1),
                FloatField("fscale_y", 3),
                FloatField("t_start", 5),
                FloatField("t_stop", 7),
                FloatField("H", 9),
            ],
        ]

        return structure


# --- /CYL_JOINT ------------------------------------------------------
@dataclass
class CylJoint(Keyword):
    joint_id: int
    joint_title: str
    node_id_1: int
    node_id_2: int
    grnd_id: int
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id:
            return f"/CYL_JOINT/{self.joint_id}/{self.unit_id}"
        else:
            return f"/CYL_JOINT/{self.joint_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("joint_title", 1, 10),
            [
                IntField("node_id_1", 1),
                IntField("node_id_2", 2),
                IntField("grnd_id", 3),
            ],
        ]

        return structure


# --- /DAMP ------------------------------------------------------
@dataclass
class Damp(Keyword):
    damp_id: int
    damp_title: str
    grnd_id: int
    skew_id: int
    t_start: float
    t_stop: float = 1.0e30
    a: float | None = None
    b: float | None = None
    ax: float | None = None
    ay: float | None = None
    az: float | None = None
    axx: float | None = None
    ayy: float | None = None
    azz: float | None = None
    bx: float | None = None
    by: float | None = None
    bz: float | None = None
    bxx: float | None = None
    byy: float | None = None
    bzz: float | None = None

    @property
    def keyword(self):
        return f"/DAMP/{self.damp_id}"

    @property
    def pre_conditions(self):
        # TODO: check consistency for short/long format definitions
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [StringField("damp_title", 1, 10)]

        # Note: it is tempting to use `all((self.a, self.b))`, but this will
        # fail if `a` or `b` equals 0 (or 0.0). We specifically want to test
        # for `None`.
        if None not in (self.a, self.b):
            structure.extend(
                [
                    [
                        FloatField("a", 1),
                        FloatField("b", 3),
                        IntField("grnd_id", 5),
                        IntField("skew_id", 6),
                        FloatField("t_start", 7),
                        FloatField("t_stop", 9),
                    ]
                ]
            )

        else:
            structure.extend(
                [
                    [
                        FloatField("ax", 1),
                        FloatField("bx", 3),
                        IntField("grnd_id", 5),
                        IntField("skew_id", 6),
                        FloatField("t_start", 7),
                        FloatField("t_stop", 9),
                    ],
                    [
                        FloatField("ay", 1),
                        FloatField("by", 3),
                    ],
                    [
                        FloatField("az", 1),
                        FloatField("bz", 3),
                    ],
                    [
                        FloatField("axx", 1),
                        FloatField("bxx", 3),
                    ],
                    [
                        FloatField("ayy", 1),
                        FloatField("byy", 3),
                    ],
                    [
                        FloatField("azz", 1),
                        FloatField("bzz", 3),
                    ],
                ]
            )

        return structure


# --- /DAMP/INTER ------------------------------------------------------
@dataclass
class DampInter(Keyword):
    """The card is intended to apply Rayleigh damping to the nodes inside of
    specified contact to increase its stability and reduce results scattering
    due to small variations of initial or boundary conditions."""

    damp_id: int
    damp_title: str
    grnd_id: int
    skew_id: int
    t_start: float
    nb_time_step: int = 20
    t_stop: float = 1.0e30
    a: float | None = None
    b: float | None = None
    ax: float | None = None
    ay: float | None = None
    az: float | None = None
    axx: float | None = None
    ayy: float | None = None
    azz: float | None = None
    bx: float | None = None
    by: float | None = None
    bz: float | None = None
    bxx: float | None = None
    byy: float | None = None
    bzz: float | None = None

    @property
    def keyword(self):
        return f"/DAMP/INTER/{self.damp_id}"

    @property
    def pre_conditions(self):
        # TODO: check consistency for short/long format definitions
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("damp_title", 1, 10),
            IntField("nb_time_step", 1),
        ]

        # Note: it is tempting to use `all((self.a, self.b))`, but this will
        # fail if `a` or `b` equals 0 (or 0.0). We specifically want to test
        # for `None`.
        if None not in (self.a, self.b):
            structure.extend(
                [
                    [
                        FloatField("a", 1),
                        FloatField("b", 3),
                        IntField("grnd_id", 5),
                        IntField("skew_id", 6),
                        FloatField("t_start", 7),
                        FloatField("t_stop", 9),
                    ]
                ]
            )

        else:
            structure.extend(
                [
                    [
                        FloatField("ax", 1),
                        FloatField("bx", 3),
                        IntField("grnd_id", 5),
                        IntField("skew_id", 6),
                        FloatField("t_start", 7),
                        FloatField("t_stop", 9),
                    ],
                    [
                        FloatField("ay", 1),
                        FloatField("by", 3),
                    ],
                    [
                        FloatField("az", 1),
                        FloatField("bz", 3),
                    ],
                    [
                        FloatField("axx", 1),
                        FloatField("bxx", 3),
                    ],
                    [
                        FloatField("ayy", 1),
                        FloatField("byy", 3),
                    ],
                    [
                        FloatField("azz", 1),
                        FloatField("bzz", 3),
                    ],
                ]
            )

        return structure


# --- /DEF_SHELL ------------------------------------------------------------------------------
@dataclass
class Def_Shell(Keyword):
    """This keyword is used to set default values for certain parameters in all shell
    properties, but options could still be changed in each property set input and
    in this case, the latter will prevail.

    """

    i_shell: Literal[0, 1, 2, 3, 4, 12, 24] = 1
    i_smstr: Literal[-2, -1, 0, 1, 2, 3, 4] = 2
    i_thick: Literal[-2, -1, 0, 1, 2] = 2
    i_plas: Literal[-2, -1, 0, 1, 2] = 2
    i_strain: Literal[0, 1, 2] = 1
    i_sh3n: Literal[0, 1, 2, 30, 31] = 2
    i_dril: Literal[0, 1, 2] = 2

    @property
    def keyword(self):
        return "/DEF_SHELL"

    @property
    def pre_conditions(self):
        conditions = []

        for attr in (
            "i_shell",
            "i_smstr",
            "i_thick",
            "i_plas",
            "i_strain",
            "i_sh3n",
            "i_dril",
        ):
            conditions.append(
                (
                    getattr(self, attr) in get_literal_values(self, attr),
                    f"Invalid value for `{attr}`. See documentation for details.",
                )
            )

        return conditions

    @property
    def structure(self):
        return [
            [
                IntField("i_shell", 1),
                IntField("i_smstr", 2),
                IntField("i_thick", 3),
                IntField("i_plas", 4),
                IntField("i_strain", 5),
                IntField("i_sh3n", 8),
                IntField("i_dril", 9),
            ]
        ]


# --- /DEF_SOLID ------------------------------------------------------
@dataclass
class Def_Solid(Keyword):
    """Used to set default values for certain parameters in all solid properties and
    thick shells. The default values defined here will be overwritten by any values
    entered on the individual property input.

    """

    i_solid: Literal[0, 1, 2, 14, 15, 16, 17, 18, 24] = 1
    i_smstr: Literal[-2, -1, 0, 1, 2, 3, 4, 10, 11, 12] = 4
    i_cpre: Literal[-2, -1, 0, 1, 2, 3] = 1
    i_tetra4: Literal[0, 1, 3, 1000] = 0
    i_tetra10: Literal[0, 2, 3, 1000] = 0
    i_mas: Literal[0, 1, 2] = 2
    i_frame: Literal[-2, -1, 0, 1, 2] = 1

    @property
    def keyword(self):
        return "/DEF_SOLID"

    @property
    def pre_conditions(self):
        conditions = []

        for attr in (
            "i_solid",
            "i_smstr",
            "i_cpre",
            "i_tetra4",
            "i_tetra10",
            "i_mas",
            "i_frame",
        ):
            conditions.append(
                (
                    getattr(self, attr) in get_literal_values(self, attr),
                    f"Invalid value for `{attr}`. See documentation for details.",
                )
            )

        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            [
                IntField("i_solid", 1),
                IntField("i_smstr", 2),
                IntField("i_cpre", 3),
                IntField("i_tetra4", 5),
                IntField("i_tetra10", 6),
                IntField("i_mas", 7),
                IntField("i_frame", 8),
            ]
        ]

        return structure


# --- /DEFAULT/INTER/TYPE2 ------------------------------------------------------
@dataclass
class DefaultInterType2(Keyword):
    """Defines interfaces TYPE2 default values."""

    ignore: Literal[0, 1, 2, 3, 1000] = 1000
    spot_flag: Literal[0, 1, 2, 4, 5, 20, 21, 22, 25, 27, 28, 30] = 5
    i_search: Literal[0, 1, 2] = 2
    i_del2: Literal[0, 1, 2, 1000] = 1000
    i_stf: Literal[0, 1, 2, 3, 4, 5] = 2

    @property
    def keyword(self):
        return "/DEFAULT/INTER/TYPE2"

    @property
    def pre_conditions(self):
        conditions = []

        for attr in ("ignore", "spot_flag", "i_search", "i_del2", "i_stf"):
            conditions.append(
                (
                    getattr(self, attr) in get_literal_values(self, attr),
                    f"Invalid value for `{attr}`. See documentation for details.",
                )
            )

        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("__blank__", 1, 10),
            [
                IntField("ignore", 3),
                IntField("spot_flag", 4),
                IntField("i_search", 6),
                IntField("i_del2", 7),
            ],
        ]

        if self.spot_flag in {25, 27, 28}:
            structure.append([IntField("i_stf", 7)])

        return structure
