#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Literal

from ..common import (
    ArrayOfAtomicFields,
    BoolField,
    FloatField,
    IntField,
    Keyword,
    KeywordStructureType,
    KeywordPreconditionsType,
    StringField,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ACCEL                      /ACTIV                      /ADMAS
# /ADMESH/GLOBAL              /ADMESH/SET                 /ADMESH/STATE/SHELL
# /ADMESH/STATE/SH3N          /ALE/BCS                    /ALE/CLOSE
#

# --- /ACCEL ----------------------------------------------------------------------------------
@dataclass
class Accel(Keyword):
    """Defines accelerometers using a node and a skew system."""

    accel_id: int
    accel_title: str
    node_id: int
    skew_id: int
    f_cut: float
    unit_id: None | int = None

    @property
    def keyword(self):
        if self.unit_id is None:
            return f"/ACCEL/{self.accel_id}"
        else:
            return f"/ACCEL/{self.accel_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("accel_title", 1, 10),
            [IntField("node_id", 1), IntField("skew_id", 2), FloatField("f_cut", 4)],
        ]

        return structure


# --- /ACTIV ----------------------------------------------------------------------------------
@dataclass
class Activ(Keyword):
    """Describes the deactivation/activation of element groups."""

    activ_id: int
    activ_title: str
    sens_id: int
    grbric_id: int
    grquad_id: int
    grshel_id: int
    grtrus_id: int
    grbeam_id: int
    grspr_id: int
    grsh3n_id: int
    i_form: Literal[1, 2] = 1
    unit_id: None | int = None
    t_start: None | float = None
    t_stop: float = 1e30

    @property
    def keyword(self):
        if self.unit_id is None:
            return f"/ACTIV/{self.activ_id}"
        else:
            return f"/ACTIV/{self.activ_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        i_form_valid = True if self.i_form in (1, 2) else False

        conditions = [
            (i_form_valid, f"Pre-condition `i_form in [1, 2]` not met."),
        ]

        if self.i_form == 2:
            t_start_is_present = True if (self.i_form == 2 and self.t_start) else False

            conditions.append(
                (
                    t_start_is_present,
                    "If `i_form == 2` then `t_start` must be provided.",
                ),
            )
        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("activ_title", 1, 10),
            [
                IntField("sens_id", 1),
                IntField("grbric_id", 2),
                IntField("grquad_id", 3),
                IntField("grshel_id", 4),
                IntField("grtrus_id", 5),
                IntField("grbeam_id", 6),
                IntField("grspr_id", 7),
                IntField("grsh3n_id", 8),
                IntField("i_form", 10),
            ],
        ]

        if self.i_form == 2:
            structure.append([FloatField("t_start", 1), FloatField("t_stop", 3)])

        return structure


# --- /ADMAS ----------------------------------------------------------------------------------
@dataclass
class Admas(Keyword):
    """Assign additional non-structural mass to nodes or a group of nodes."""

    admas_id: int
    admas_title: str
    type: Literal[0, 1, 2, 3, 4, 5, 6, 7]
    unit_id: None | int = None
    mass: None | float | List[float] = None
    grnd_id: None | int = None
    surf_id: None | int = None
    grpart_id: None | int = None
    mass_per_unit_area: None | float = None
    node_id: None | List[int] = None
    part_id: None | List[int] = None
    iflag: None | Literal[0, 1] | List[Literal[0, 1]] = 0

    @property
    def keyword(self):
        if self.unit_id is None:
            return f"/ADMAS/{self.type}/{self.admas_id}"
        else:
            return f"/ADMAS/{self.type}/{self.admas_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        conditions: KeywordPreconditionsType = [
            (
                self.type in {0, 1, 2, 3, 4, 5, 6, 7},
                "Pre-condition `type in [0, 1, 2, 3, 4, 5, 6, 7]` not met.",
            ),
        ]

        if self.type in {3, 4}:
            conditions.append(
                (
                    self.iflag in {0, 1},
                    "Pre-condition `iflag in [0, 1]` not met.",
                ),
            )

        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [StringField("admas_title", 1, 10)]

        if self.type in (0, 1):
            structure.append([FloatField("mass", 1), IntField("grnd_id", 3)])

        elif self.type == 2:
            structure.append(
                [FloatField("mass_per_unit_area", 1), IntField("surf_id", 3)]
            )

        elif self.type in (3, 4):
            structure.append(
                [
                    FloatField("mass", 1),
                    IntField("grpart_id", 3),
                    IntField("iflag", 4),
                ]
            )

        elif self.type == 5:

            structure.append(
                ArrayOfAtomicFields([FloatField("mass", 1), IntField("node_id", 3)])
            )

        elif self.type in (6, 7):
            structure.append(
                ArrayOfAtomicFields(
                    [
                        FloatField("mass", 1),
                        IntField("part_id", 3),
                        IntField("iflag", 4),
                    ]
                )
            )

        return structure


# --- /ADMESH/GLOBAL ------------------------------------------------------
@dataclass
class AdmeshGlobal(Keyword):
    """Defines the global parameters for adaptive meshing."""

    levelmax: int
    ladmrule: Literal[0, 1]
    time_delay: float
    idt: Literal[0, 1]

    @property
    def keyword(self):
        return "/ADMESH/GLOBAL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            [
                IntField("levelmax", 1),
                IntField("ladmrule", 2),
                FloatField("time_delay", 3),
                IntField("idt", 5),
            ]
        ]

        return structure


# --- /ADMESH/SET ------------------------------------------------------
@dataclass
class AdmeshSet(Keyword):
    """Defines the criteria for adaptive meshing in parts."""

    adset_id: int
    adset_title: str
    angle_criterion: float
    inilev: int
    thkerr: float
    part_ids: List[int]

    @property
    def keyword(self):
        return f"/ADMESH/SET/{self.adset_id}"

    @property
    def pre_conditions(self):
        return [
            (len(self.part_ids) > 0, "Pre-condition `len(part_ids) > 0` is violated."),
            (len(self.part_ids) <= 10, "Pre-condition `len(part_ids)` is violated."),
            (self.inilev > 0, "Pre-condition `inilev > 0` is violated."),
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("adset_title", 1, 10),
            [
                FloatField("angle_criterion", 1),
                IntField("inilev", 3),
                FloatField("thkerr", 4),
            ],
            [IntField(f"part_ids:{i}", i + 1) for i in range(len(self.part_ids))],
        ]

        return structure


# --- /ADMESH/STATE/SHELL ------------------------------------------------------
@dataclass
class AdmeshStateShell(Keyword):
    """Describes the state of shells in adaptive meshing."""

    shell_id: int
    shell_id1: int
    shell_id2: int
    shell_id3: int
    shell_id4: int
    actlev: int
    imapping: Literal[-1, 0, 1]

    @property
    def keyword(self):
        return "/ADMESH/STATE/SHELL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            [
                IntField("shell_id", 1),
                IntField("shell_id1", 2),
                IntField("shell_id2", 3),
                IntField("shell_id3", 4),
                IntField("shell_id4", 5),
                IntField("actlev", 6),
                IntField("imapping", 7),
            ]
        ]

        return structure


# --- /ADMESH/STATE/SH3N ------------------------------------------------------
@dataclass
class AdmeshStateSh3n(Keyword):
    """Describes the state of 3-node shells in a multi-stage analysis using
    adaptive meshing."""

    sh3n_id: int
    sh3n_id1: int
    sh3n_id2: int
    sh3n_id3: int
    sh3n_id4: int
    actlev: int
    imapping: Literal[-1, 0, 1]

    @property
    def keyword(self):
        return "/ADMESH/STATE/SH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            [
                IntField("sh3n_id", 1),
                IntField("sh3n_id1", 2),
                IntField("sh3n_id2", 3),
                IntField("sh3n_id3", 4),
                IntField("sh3n_id4", 5),
                IntField("actlev", 6),
                IntField("imapping", 7),
            ]
        ]

        return structure


# --- /ALE/BCS ------------------------------------------------------
@dataclass
class ALEBcs(Keyword):
    """Describes the ALE boundary conditions."""

    bcs_id: int
    bcs_title: float
    grilag: List[Literal[0, 1]]
    skew_id: int
    grnd_id: int

    @property
    def keyword(self):
        return f"/ALE/BCS/{self.bcs_id}"

    @property
    def pre_conditions(self):
        return [
            (len(self.grilag) == 6, "Pre-condition `len(grilag) == 6` is violated.")
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("bcs_title", 1, 10),
            [
                BoolField("grilag", 1, 6, [4, 5, 6, 8, 9, 10]),
                IntField("skew_id", 2),
                IntField("grnd_id", 3),
            ],
        ]

        return structure


# --- /ALE/CLOSE ------------------------------------------------------
@dataclass
class ALEClose(Keyword):
    """Describes the treatment of element closure."""

    prop_id: int
    htest: float
    hclose: None | float = None

    def __post_init__(self):
        super().__post_init__()
        if self.hclose is None:
            self.hclose = 0.1 * self.htest

    @property
    def keyword(self):
        return f"/ALE/CLOSE/{self.prop_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            [FloatField("htest", 1), FloatField("hclose", 3)]
        ]

        return structure
