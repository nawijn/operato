#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal, List
from numpy.typing import NDArray

from ..common import (
    ArrayOfAtomicFields,
    BoolField,
    FloatField,
    IntField,
    Keyword,
    StringField,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ALE/MUSCL                  /ALE/SOLVER/FINT            /AMS
# /ANALY                      /ANIM/VERS                  /BCS
# /BCS/CYCLIC                 /BCS/LAGMUL                 /BEAM
#

# --- /ALE/MUSCL ------------------------------------------------------------------------------
@dataclass
class ALEMuscl(Keyword):
    """Allows for a second order monotonic upstream-centered scheme for
    conservation laws (MUSCL) reconstruction of volume fraction fields when
    using multi-material laws and for full full second order scheme (time and
    space) when using material law LAW151."""

    beta: float
    iflag: Literal[0, 1] = 0

    @property
    def keyword(self):
        return "/ALE/MUSCL"

    @property
    def pre_conditions(self):
        return [
            (0.0 < self.beta < 2.0, "Pre-condition `0.0 < beta < 2.0` is violated.")
        ]

    @property
    def structure(self):
        structure = [[FloatField("beta", 1), IntField("iflag", 3)]]

        return structure


# --- /ALE/SOLVER/FINT ------------------------------------------------------------------------
@dataclass
class ALESolverFint(Keyword):
    """This option defines the numerical method for internal force
    integration.  This is relevant only for brick element and ALE legacy solver
    (momentum equation solved with FEM)."""

    iform: Literal[0, 1, 2, 3] = 3

    @property
    def keyword(self):
        return "/ALE/SOLVER/FINT"

    @property
    def pre_conditions(self):
        return [
            (
                self.iform in {0, 1, 2, 3},
                "Pre-condition `iform in {0,1,2,3} is violated.",
            )
        ]

    @property
    def structure(self):
        structure = [IntField("iform", 1)]

        return structure


# --- /AMS ------------------------------------------------------------------------------------
@dataclass
class Ams(Keyword):
    """Describes the part group on which the advanced mass scaling is applied."""

    grpart_id: int

    @property
    def keyword(self):
        return "/AMS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [IntField("grpart_id", 1)]

        return structure


# --- /ANALY ----------------------------------------------------------------------------------
@dataclass
class Analy(Keyword):
    """Defines the type of analysis and sets analysis flags."""

    n_2D3D: Literal[0, 1, 2] = 0
    i_parith: Literal[0, 1, 2] = 0
    i_subcycle: Literal[0, 2] = 0

    @property
    def keyword(self):
        return "/ANALY"

    @property
    def pre_conditions(self):
        return [
            (
                self.n_2D3D in {0, 1, 2},
                "Pre-condtion `n_2D3D in {0, 1, 2} is violated.",
            ),
            (
                self.i_parith in {0, 1, 2},
                "Pre-condtion `i_parith in {0, 1, 2} is violated.",
            ),
            (
                self.i_subcycle in {0, 2},
                "Pre-condtion `i_subcycle in {0, 2} is violated.",
            ),
        ]

    @property
    def structure(self):
        return [
            [
                IntField("n_2D3D", 1),
                IntField("i_parith", 3),
                IntField("i_subcycle", 4),
            ]
        ]


# --- /ANIM/VERS ------------------------------------------------------------------------------
@dataclass
class AnimVers(Keyword):
    """Defines the animation file version."""

    anim_vers: int = 44

    @property
    def keyword(self):
        return "/ANIM/VERS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [IntField("anim_vers", 1)]

        return structure


# --- /BCS ------------------------------------------------------------------------------------
@dataclass
class Bcs(Keyword):
    """Defines boundary conditions on node groups for translational and rotational motion."""

    bcs_id: int
    bcs_title: str
    trarot: str
    skew_id: int
    grnd_id: int

    @property
    def keyword(self):
        return f"/BCS/{self.bcs_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("bcs_title", 1, 10),
            [
                BoolField("trarot", 1, 6, [4, 5, 6, 8, 9, 10]),
                IntField("skew_id", 2),
                IntField("grnd_id", 3),
            ],
        ]

        return structure


# --- /BCS/CYCLIC -----------------------------------------------------------------------------
@dataclass
class BcsCyclic(Keyword):
    """Defines a cyclic boundary condition on a structure in a fixed
    cylindrical coordinate system."""

    bcs_id: int
    bcs_cyclic_title: str
    grnd_id_1: int
    grnd_id_2: int
    skew_id: int = 0

    @property
    def keyword(self):
        return f"/BCS/{self.bcs_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("bcs_cyclic_title", 1, 10),
            [
                IntField("skew_id", 1),
                IntField("grnd_id_1", 2),
                IntField("grnd_id_2", 3),
            ],
        ]

        return structure


# --- /BCS/LAGMUL ------------------------------------------------------
@dataclass
class BcsLagmul(Keyword):
    """Defines boundary conditions on node groups using Lagrange multipliers.
    This keyword is not available for SPMD computation."""

    bcs_id: int
    bcs_title: str
    trarot: str
    skew_id: int
    grnd_id: int

    @property
    def keyword(self):
        return f"/BCS/{self.bcs_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("bcs_title", 1, 10),
            [
                BoolField("trarot", 1, 6, [4, 5, 6, 8, 9, 10]),
                IntField("skew_id", 2),
                IntField("grnd_id", 3),
            ],
        ]

        return structure


# --- /BEAM ------------------------------------------------------
@dataclass
class Beam(Keyword):
    """Describes the beam elements. Two properties (/PROP/TYPE3 (BEAM) and
    /PROP/TYPE18 (INT_BEAM)) are available for this beam element. The
    properties describing a beam element are all defined in a local beam
    coordinate system.
    """

    part_id: int
    beam_ids: List[int]
    node_ids: NDArray

    @property
    def keyword(self):
        return f"/BEAM/{self.part_id}"

    @property
    def pre_conditions(self):
        return [
            (
                len(self.beam_ids) == len(self.node_ids),
                "Pre-condition `len(beam_ids) == len(node_ids)` is violated.",
            )
        ]

    @property
    def structure(self):
        structure = [
            ArrayOfAtomicFields(
                [
                    IntField("beam_ids", 1),
                    IntField("node_ids:ID_1|0", 2),
                    IntField("node_ids:ID_2|1", 3),
                    IntField("node_ids:ID_3|2", 4),
                ]
            )
        ]

        return structure
