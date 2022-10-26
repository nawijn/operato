#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal

from ..common import (
    BoolField,
    FloatField,
    IntField,
    Keyword,
    KeywordStructureType,
    StringField,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /EIG                        /ENCRYPT                    /END
# /EOS/COMPACTION             /EOS/GRUNEISEN              /EOS/IDEAL-GAS
# /EOS/IDEAL-GAS-VT           /EOS/LINEAR                 /EOS/LSZK
#

# --- /EIG ------------------------------------------------------
@dataclass
class Eig(Keyword):
    """Defines the eigen modes and static modes computation for flexible bodies."""

    eig_id: int
    eig_title: str
    trarot: str
    ifile: Literal[0, 1]
    cutfreq: float  # TODO: maybe check source code if cutfreq is indeed a float.
    nbloc: int
    grnd_id: int = 0
    grnd_bc: int = 0
    nmod: int = 100
    inorm: int = 0
    incv: int = 2
    freqmin: float = 0.045
    ipri: int = 0
    niter: int = 300
    tol: float = 0.0
    filename: str | None = None
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id is None:
            return f"/EIG/{self.eig_id}"
        else:
            return f"EIG/{self.eig_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("eig_title", 1, 10),
            [
                IntField("grnd_id", 1),
                IntField("grnd_bc", 2),
                BoolField("trarot", 3, 6, [4, 5, 6, 8, 9, 10]),
                IntField("ifile", 4),
            ],
            [
                IntField("nmod", 1),
                IntField("inorm", 2),
                FloatField("cutfreq", 3),
                FloatField("freqmin", 5),
            ],
            [
                IntField("nbloc", 1),
                IntField("incv", 2),
                IntField("niter", 3),
                IntField("ipri", 4),
                FloatField("tol", 5),
            ],
        ]

        if self.ifile == 1:
            structure.append(StringField("filename", 1, 10))

        return structure


# --- /ENCRYPT ------------------------------------------------------
@dataclass
class Encrypt(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ENCRYPT` is not implemented.")

    @property
    def keyword(self):
        return "/ENCRYPT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /END ------------------------------------------------------
@dataclass
class End(Keyword):
    """Declares that end of input deck has been reached."""

    @property
    def keyword(self):
        return "/END"


# --- /EOS/COMPACTION ------------------------------------------------------
@dataclass
class EosCompaction(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/COMPACTION` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/COMPACTION"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EOS/GRUNEISEN ------------------------------------------------------
@dataclass
class EosGruneisen(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/GRUNEISEN` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/GRUNEISEN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EOS/IDEAL-GAS ------------------------------------------------------
@dataclass
class EosIdealGas(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/IDEAL-GAS` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/IDEAL-GAS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EOS/IDEAL-GAS-VT ------------------------------------------------------
@dataclass
class EosIdealGasVt(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/IDEAL-GAS-VT` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/IDEAL-GAS-VT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EOS/LINEAR ------------------------------------------------------
@dataclass
class EosLinear(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/LINEAR` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/LINEAR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EOS/LSZK ------------------------------------------------------
@dataclass
class EosLszk(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/EOS/LSZK` is not implemented.")

    @property
    def keyword(self):
        return "/EOS/LSZK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
