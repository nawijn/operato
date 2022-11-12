#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal

from ..common import BoolField, FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ALE/GRID/DISP              /ALE/GRID/DONEA             /ALE/GRID/LAPLACIAN
# /ALE/GRID/SPRING            /ALE/GRID/STANDARD          /ALE/GRID/VOLUME
# /ALE/GRID/ZERO              /ALE/LINK/VEL               /ALE/MAT
#

# --- /ALE/GRID/DISP --------------------------------------------------------------------------
@dataclass
class ALEGridDisp(Keyword):
    """Displacement of a grid node depends on the displacement of neighboring
    grid nodes."""

    u_max: float = -1.0e30
    v_min: float = -1.0e30

    @property
    def keyword(self):
        return "/ALE/GRID/DISP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [FloatField("u_max", 1), FloatField("v_min", 1)]

        return structure


# --- /ALE/GRID/DONEA -------------------------------------------------------------------------
@dataclass
class ALEGridDonea(Keyword):
    """Velocity of a given grid node depends on velocity and displacements of
    neighboring grid nodes."""

    alpha: float = 0.0
    gamma: float = 100.0
    fscale_x: float = 1.0
    fscale_y: float = 1.0
    fscale_z: float = 1.0
    v_min: float = -1.0e30

    @property
    def keyword(self):
        return "/ALE/GRID/DONEA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            [
                FloatField("alpha", 1),
                FloatField("gamma", 3),
                FloatField("fscale_x", 5),
                FloatField("fscale_y", 7),
                FloatField("fscale_z", 9),
            ],
            FloatField("v_min", 1),
        ]

        return structure


# --- /ALE/GRID/LAPLACIAN ---------------------------------------------------------------------
@dataclass
class ALEGridLaplacian(Keyword):
    """ALE grid smoothing using the laplacian smoothing method for 2D and 3D
    elements.

    NOTE: an attribute name of `lambda` (reflecting the documentation of
    OpenRadioss) is not allowed in Python. Therefore the attribute is renamed
    to `scale_factor`.
    """

    # `lambda` is unfortunately not allowed here.
    scale_factor: float = 1.0
    n_iter: int = 1

    @property
    def keyword(self):
        return "/ALE/GRID/LAPLACIAN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [[FloatField("scale_factor", 1), IntField("n_iter", 3)]]

        return structure


# --- /ALE/GRID/SPRING ------------------------------------------------------------------------
@dataclass
class ALEGridSpring(Keyword):
    """Grid nodes connected with nonlinear springs."""

    dt_0: float
    gamma: float = 0.0
    eta: float = 0.5
    nu: float = 1.0
    v_min: float = -1.0e30

    @property
    def keyword(self):
        return "/ALE/GRID/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            [
                FloatField("dt_0", 1),
                FloatField("gamma", 3),
                FloatField("eta", 5),
                FloatField("nu", 7),
            ],
            FloatField("v_min", 1),
        ]

        return structure


# --- /ALE/GRID/STANDARD ----------------------------------------------------------------------
@dataclass
class ALEGridStandard(Keyword):
    """Describes the standard formulation for ALE grid velocity computation."""

    l_c: float
    alpha: float = 0.9
    gamma: float = 1.0e-2
    eta: float = 1e-2

    @property
    def keyword(self):
        return "/ALE/GRID/STANDARD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            [
                FloatField("alpha", 1),
                FloatField("gamma", 3),
                FloatField("eta", 5),
                FloatField("l_c", 7),
            ]
        ]

        return structure


# --- /ALE/GRID/VOLUME ------------------------------------------------------------------------
@dataclass
class ALEGridVolume(Keyword):
    """ALE grid smoothing formulation based on volume. Each ALE node position
    is computed as the average position of the centroids of the elements to
    which it is connected."""

    @property
    def keyword(self):
        return "/ALE/GRID/VOLUME"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        # This keyword has not attributes.
        structure = []

        return structure


# --- /ALE/GRID/ZERO --------------------------------------------------------------------------
@dataclass
class ALEGridZero(Keyword):
    """Describes the Euler formulation."""

    @property
    def keyword(self):
        return "/ALE/GRID/ZERO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        # This keyword has not attributes.
        structure = []

        return structure


# --- /ALE/LINK/VEL ---------------------------------------------------------------------------
@dataclass
class ALELinkVel(Keyword):
    """With ALE links on grid velocities, given nodes are linked to the given main grid
    velocities. Either a direction or a combination of directions can be specified."""

    alelink_id: int
    alelink_title: str
    node_id_1: int
    node_id_2: int
    grnod_id: int
    grid_dof: str
    i_form: Literal[-1, 0, 1]
    t_start: float
    t_stop: float

    @property
    def keyword(self):
        return f"/ALE/LINK/VEL/{self.alelink_id}"

    @property
    def pre_conditions(self):
        return [
            (
                self.i_form in {-1, 0, 1},
                "Pre-condition `i_form in {-1, 0, 1}` violated.",
            )
        ]

    @property
    def structure(self):
        structure = [
            StringField("alelink_title", 1, 10),
            [
                IntField("node_id_1", 1),
                IntField("node_id_2", 2),
                IntField("grnod_id", 3),
                BoolField("grid_dof", 4, 3, [4, 5, 6]),
                IntField("i_form", 5),
            ],
            [FloatField("t_start", 1), FloatField("t_stop", 3)],
        ]

        return structure


# --- /ALE/MAT --------------------------------------------------------------------------------
@dataclass
class ALEMat(Keyword):
    """Compute material flow with ALE framework."""

    mat_id: int

    @property
    def keyword(self):
        return f"/ALE/MAT/{self.mat_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        # This keyword has not attributes.
        structure = []

        return structure
