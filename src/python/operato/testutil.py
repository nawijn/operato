from io import StringIO
from pathlib import Path
from typing import Type
import json
from colorama import Fore, Style
from operato.keywords.common import Keyword, TextAlignment
import toml


def h1(text):
    """Style for header like line."""
    style = Fore.LIGHTYELLOW_EX
    text = f" {text} ".center(100, "=")
    reset = Style.RESET_ALL
    return f"{style}{text}{reset}"


def mark(text):
    """Style for marking (highlighting) a text."""
    style = Style.BRIGHT
    text = f" {text} ".center(100)
    reset = Style.RESET_ALL
    return f"{style}{text}{reset}"


class IOBuffer(StringIO):
    """Wrapper around a standard `StringIO` buffer. This class has adds one additional
    method `reset` and modifies the return value of `getvalue` (it replaces spaces with
    underscores, so it is easier to debug a formatted keyword)."""

    def reset(self):
        """Resets the buffer."""
        self.seek(0)
        self.truncate()

    def getvalue(self):
        """Returns the contents of the buffer. Spaces are replaced by an underscore."""
        return super().getvalue().replace(" ", "_")


class TestManager:
    """Provides a small utitlity class to facilitate testing and showing keyword definitions."""

    def __init__(self, keyword_definitions_folder: Path):
        if not keyword_definitions_folder.is_dir():
            raise IOError(f"Folder `{keyword_definitions_folder}` does not exist.")

        self.keyword_definitions_folder = keyword_definitions_folder

        # Set the keyword class
        self._keyword_class: None | Type[Keyword] = None
        self._keyword_definition: None | dict = None

    def set_keyword_class(self, keyword_class: Type[Keyword]):
        self._keyword_class = keyword_class

    def load_keyword_definition(self):

        if self._keyword_class is None:
            raise RuntimeError("Keyword class `_keyword_class` not defined (bug).")

        keyword_definition_path = self.keyword_definitions_folder.joinpath(
            f"test_{self._keyword_class.__name__.lower()}.toml"
        )

        if not keyword_definition_path.is_file():
            raise FileNotFoundError(f"File `{keyword_definition_path}` does not exist.")

        self._keyword_definition = toml.load(keyword_definition_path)

    def show_definition(self):
        print(json.dumps(self._keyword_definition, indent=2, sort_keys=True))

    def _process_definition(self, check_value=False):
        buffer = IOBuffer()

        if not self._keyword_definition:
            raise RuntimeError("`_keyword_definition == None` (BUG) ")

        if not self._keyword_class:
            raise RuntimeError("`_keyword_class == None` (BUG) ")

        keyword_definition = self._keyword_definition

        sections = sorted(keyword_definition.keys())

        print(h1(self._keyword_class.__name__))

        for section in sections:
            default_definition = keyword_definition["default"]
            section_definition = keyword_definition[section]

            print(mark(section))

            if "control" in section_definition:
                mode = section_definition["control"]["mode"]
            else:
                mode = "update"

            if mode not in ("replace", "update"):
                raise ValueError(
                    f"`mode` must be either `update` or `replace`, not `{mode}`"
                )

            if mode == "update":
                params = default_definition["params"]
                params.update(section_definition["params"])
            else:
                params = section_definition["params"]

            obj = self._keyword_class(**params)
            # Adjust alignment
            obj.set_float_alignment(TextAlignment.RIGHT)
            obj.set_int_alignment(TextAlignment.RIGHT)

            obj.write(buffer)

            if check_value:
                value = keyword_definition[section].get("value", None)
                if value:
                    assert (
                        buffer.getvalue() == value
                    ), f"({self._keyword_class.__name__}, {section})"

            else:
                print(buffer.getvalue())

            buffer.reset()

    def show_keyword(self, check_value=False):
        self._process_definition(check_value)

    def test_keyword(self, check_value=True):
        self._process_definition(check_value)

    def reset(self):
        self._keyword_class = None
        self._keyword_definition = None
