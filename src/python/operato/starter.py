#!/usr/bin/env python3
"""Provides a low-level interface for generating OpenRadioss starter files.

"""
from pathlib import Path

from .keywords import KEYWORD_REGISTRY
from ._keywords.common import Keyword


class Starter:
    """Represents the starter part of an OpenRadioss simulation. It features a
    very natural syntax for selecting keyword templates and providing them with
    the parameters they need for instantation:

    >>> starter[<keyword>](<kwargs>)

    For example:
    >>> starter["BEGIN"](runname="Crash test")


    """

    def __init__(self):
        """Initializes a new starter instance."""

        # The keyword registry containing all OpenRadioss starter keywords.
        # The key is the name of the keyword in uppercase ("ADMESH/GLOBAL")
        # without the leading "/".
        self._keyword_registry = KEYWORD_REGISTRY["starter"]
        self._keywords = []
        self._active_keyword_cls = None
        self._runname = None

    @property
    def runname(self):
        return self._runname

    def __getitem__(self, key):
        """Mimics attribute access to a keyword, but always returns `self`. It
        does set the active keyword class, so when calling `self`, it
        instantiates the correct class."""
        self._active_keyword_cls = self._keyword_registry[key.lstrip("/").upper()]
        return self

    def __call__(self, **kwargs) -> Keyword:
        """Instantiates the current active keyword class with the provided arguments."""

        if not self._active_keyword_cls:
            raise RuntimeError(
                "Call operator must be called with `_active_keyword_cls` set."
            )

        cls = self._active_keyword_cls

        if not self._runname:
            if not cls == self._keyword_registry["BEGIN"]:
                raise RuntimeError("The first keyword must be `BEGIN`")

            self._runname = kwargs["runname"]

        instance = cls(**kwargs)

        self._keywords.append(instance)

        return instance

    def write(
        self, index=0, folder: str | Path | None = None, assume_yes=False
    ) -> None:
        """Writes the keywords to a file."""
        if folder is None:
            folder = Path().cwd()
        elif isinstance(folder, str):
            folder = Path(folder)

        filepath = folder.joinpath(f"{self.runname}_{index:04d}.rad")

        if filepath.is_file() and not assume_yes:
            overwrite_file = input(
                f"File `{filepath}` already exists. Overwrite? [yes/no (default=no)] "
            )

            if not overwrite_file.lower() in ("y", "yes"):
                return

        # Serialize the keywords
        with open(filepath, "w") as fd:
            for keyword in self._keywords:
                keyword.write(fd)


if __name__ == "__main__":
    pass
