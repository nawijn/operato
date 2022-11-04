from abc import abstractproperty
from collections import namedtuple
from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum
from io import TextIOBase
from math import floor
from typing import List, Iterable, Literal, Sequence, Tuple, get_args, get_type_hints

import numpy as np

from operato.constants import (
    FIELDWIDTH,
    FLOAT_FULL_FORMAT_SPEC,
    INT_FULL_FORMAT_SPEC,
    NFIELDS,
)


# Collects column indexing information for fields that reference array like
# objects
ArrayInfo = namedtuple("ArrayInfo", ("attr", "column_index", "index_style"))

# --- Small utility functions -----------------------------------------------------------------
def get_literal_values(obj, attr):
    """Small utility to extract the values from a `Literal` type hint."""
    return get_args(get_type_hints(obj)[attr])


def check_if_all_values_are_present(
    obj, sequence_of_attrs
) -> Tuple[Literal[True], None] | Tuple[Literal[False], str]:

    attrs_that_are_none = []
    for attr in sequence_of_attrs:
        if getattr(obj, attr) is None:
            attrs_that_are_none.append(attr)

    if len(attrs_that_are_none) == 0:
        return (True, None)
    else:
        srep = ", ".join(attrs_that_are_none)
        return (False, srep)


def has_shape(array_like, shape):
    """Small utility to whether or not the shape (number of rows/columns) of
    the `array_like` object matches `shape`. Note that the `shape` parameter
    must be fully defined. So if it has 3 rows and 1 column, the shape is (3,
    1) and not (3,). The latter is what Numpy returns for a 1 dimensional
    array."""

    if not isinstance(array_like, np.ndarray):
        array_like = np.array(array_like)

    array_like_shape = array_like.shape
    # Handle the 1D case where numpy indicates the shape as (nrows,).
    if len(array_like_shape) == 1:
        array_like_shape = (array_like_shape[0], 1)

    return array_like_shape == shape


def has_no_nones(iterable: Iterable):
    """Small utility to check whether or not an iterable has None values."""
    for element in iterable:
        if element is None:
            return False
    return True


def has_all_nones(iterable: Iterable):
    """Small utility to check whether or not all elements in `iterable` are
    None."""
    for element in iterable:
        if element is not None:
            return False

    return True


def is_exclusive(*args) -> Literal[True, False]:
    """Check if only 1 of the elements in the sequence has a value other than
    None."""

    if not args:
        raise RuntimeError("Expecting a sequence with at least 1 element.")

    if all([isinstance(arg, Iterable) for arg in args]):
        flags = [not has_all_nones(arg) for arg in args]
        return flags.count(True) == 1
    else:
        return args.count(None) == len(args) - 1


def have_same_length(*args) -> Literal[True, False]:
    """Very simple algoritm. Collect the lengths of all array like objects in
    `seq`.  Add those lengths to a set (duplicates are not stored in a set) and
    make sure there is only 1 element in the set."""
    return len(set([len(element) for element in args])) == 1


class KeywordCategory(Enum):
    """Helper enumeration in case we need to distinguish between whether or not
    a particular keyword is an engine, starter or generic keyword. Generic in
    this case means the keyword does not need special treatment.

    The reason why this enumaration is added is to gracefully handle the case
    where an engine keyword uses more than 5 float fields on a single line
    (e.g. `/ALE/DISP/DONEA`)."""

    ENGINE = 1
    STARTER = 2
    GENERIC = 3


class LineDefinitionType(Enum):
    # Example: `StringField(..)`
    SINGLE_ATOMIC_FIELD = 1

    # Example: `[IntField(..), FloatField(..), FloatField(..)]`
    SEQUENCE_OF_ATOMIC_FIELDS = 2

    # Example: `VLSequenceOfAtomicField(IntField(..))`
    VL_SEQUENCE_OF_ATOMIC_FIELD = 3

    # Example: `ArrayOfAtomicFields([IntField(..), FloatField(..),
    # FloatField(..)])`
    ARRAY_OF_ATOMIC_FIELDS = 4

    # Example: `MultiLineArrayOfAttomicFields( [ArrayOfAtomicFields(..),
    # ArrayOfAtomicFields(..)])`
    MULTI_LINE_ARRAY_OF_ATOMIC_FIELDS = 5


class TextAlignment(Enum):
    """Options for text alignment in a field."""

    LEFT = 1
    CENTER = 2
    RIGHT = 3


class IndexStyle(Enum):
    """Identifies the column indexing style for keyword fields that reference
    array like objects."""

    BY_COLUMN_INDEX = 1
    BY_NAME = 2
    NONE = 3


# --- Field definitions -----------------------------------------------------------------------
#
# For each of the Radioss keywords, its structure and the type of each field in
# the keyword must be defined. This is done by specifying, for each keyword, a
# sequence of field types.  Each field type contains information about the
# underlying type (bool, float, int, str), where the field is located in the
# keyword and how wide the field is/can be.


@dataclass
class BoolField:
    """Represents a single boolean flag field in a keyword."""

    attr: str
    index: int
    nflags: int
    positions: List[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

    @property
    def span(self) -> Literal[1]:
        return 1

    def __call__(self, values) -> str:
        if len(values) != self.nflags:
            raise ValueError("Condition `len(values) != nflags` is violated.")

        flags = 10 * [" "]
        for position, value in zip(self.positions, values):
            if value not in (0, 1):
                raise ValueError("Boolean values must be either 0 or 1.")

            # Flag indices follow the documentation, so they start at `1`, we
            # need to compensate for this when assigning them to a position in
            # a Python list.
            flags[position - 1] = f"{value}"

        return "".join(flags)


@dataclass
class FloatField:
    """Represents a single string field in a keyword."""

    attr: str
    index: int

    @property
    def span(self) -> Literal[2]:
        return 2

    def __call__(self, value) -> str:
        if value is None:
            return ""

        srep = FLOAT_FULL_FORMAT_SPEC.format(value=value)

        if len(srep) > 20:
            raise ValueError(f"Float value `{value}` for `{self.attr}` is too large.")
        return srep


@dataclass
class IntField:
    """Represents a single string field in a keyword."""

    attr: str
    index: int

    @property
    def span(self) -> Literal[1]:
        return 1

    def __call__(self, value) -> str:
        if value is None:
            return ""

        srep = INT_FULL_FORMAT_SPEC.format(value=value)

        if len(srep) > 9:
            raise ValueError(f"Integer value `{value}` for `{self.attr}` is too large.")
        return srep


@dataclass
class StringField:
    """Represents a single string field in a keyword."""

    attr: str
    index: int
    span: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    alignment: TextAlignment | None = None

    def __call__(self, value: str) -> str:
        if len(value) > self.span * FIELDWIDTH:
            raise ValueError(f"String value `{value}` for `{self.attr}` is too large.")
        return value


@dataclass
class VLSequenceOfAtomicField:
    """Represents a variable length of fields of a single atomic type. This
    field is typically used for the definition of lists of
    boxes/parts/nodes/elements (see /BOX/BOX for an example)."""

    field: IntField | FloatField


@dataclass
class ArrayOfAtomicFields:
    """Represents the fields in keywords that are arrays (like /NODE).

    When a field is defined inside a `ArrayOfAtomicFields` object, the `attr`
    argument must follow a particular pattern in case of a multi-dimensional
    array. For example, the `xc` field in the /NODE keyword is defined as
    `FloatField("xc_yc_zc:0")` where `xc_yc_zc` is the Nx3 Numpy array holding
    the coordinates and `0` is the column index of this array that corresponds
    to the `xc` coordinate.

    """

    fields: Sequence[IntField | FloatField]

    @property
    def span(self) -> int:
        return sum([field.span for field in self.fields])


@dataclass
class MultiLineArrayOfAtomicFields:
    """Represents the fields in a keyword that are array like, but where each entry
    consists of more than one line (for example /BRIC20)."""

    fields: Sequence[ArrayOfAtomicFields]


# Type aliases for return values or local parameters
KeywordPreconditionsType = List[Tuple[bool, str]]

AtomicFields = BoolField | FloatField | IntField | StringField

ListOfAtomicFields = List[AtomicFields]

KeywordStructureType = List[
    AtomicFields
    | ListOfAtomicFields
    | ArrayOfAtomicFields
    | MultiLineArrayOfAtomicFields
    | VLSequenceOfAtomicField
]


def get_line_definition_type(line_definition) -> LineDefinitionType:

    if not isinstance(line_definition, Sequence):
        cls_name = line_definition.__class__.__name__
        match cls_name:
            case "BoolField" | "FloatField" | "IntField" | "StringField":
                return LineDefinitionType.SINGLE_ATOMIC_FIELD
            case "ArrayOfAtomicFields":
                return LineDefinitionType.ARRAY_OF_ATOMIC_FIELDS
            case "MultiLineArrayOfAtomicFields":
                return LineDefinitionType.MULTI_LINE_ARRAY_OF_ATOMIC_FIELDS
            case "VLSequenceOfAtomicField":
                return LineDefinitionType.VL_SEQUENCE_OF_ATOMIC_FIELD

    all_atomic = True
    for entry in line_definition:
        if not isinstance(entry, (BoolField, FloatField, IntField, StringField)):
            all_atomic = False

    if all_atomic:
        return LineDefinitionType.SEQUENCE_OF_ATOMIC_FIELDS

    raise RuntimeError("Invalid line definition (BUG)")


# --- Starter keywords ------------------------------------------------------------------------
@dataclass
class Keyword:
    """Baseclass for OpenRadioss keyword definitions."""

    def __post_init__(self) -> None:
        self._text_alignment = {
            # Note: specifying an alignment for a `BoolField` has no effect
            # because the string representation of a `BoolField` is always
            # exactly 10 characters (so, as wide as the field). Add it here,
            # because it allows us to process the fields regardless of its
            # specific type.
            BoolField: TextAlignment.CENTER,
            FloatField: TextAlignment.CENTER,
            IntField: TextAlignment.CENTER,
            StringField: TextAlignment.LEFT,
        }

        # Both starter and engine keywords can be treated in the same way if
        # the keyword category equals `KeywordCategory.GENERIC`. If either a
        # starter or an engine keyword needs special treatment, use
        # `KeywordCategory.STARTER` or `KeywordCategory.ENGINE` respectively.
        self.category: KeywordCategory = KeywordCategory.GENERIC

    def check_pre_conditions(self) -> None:
        """Check pre-conditions for this keyword.

        Check pre-conditions for this keyword. Raises a `RuntimeError` exception when any
        pre-condition is violated.

        """

        for condition_holds, message in self.pre_conditions:
            if not condition_holds:
                raise RuntimeError(message)

    @property
    def pre_conditions(self) -> KeywordPreconditionsType:
        """State a sequence of conditions that must evaluate to `True` prior to generating
        the text content of this keyword.

        """
        return []

    @abstractproperty
    def structure(self) -> KeywordStructureType:
        """Return the structure of the (concrete) keyword. This property must be
        implemented by derived classes.
        """
        return []

    @abstractproperty
    def keyword(self) -> str:
        """The keyword label (starting line of the keyword block). This property must be
        implemented by derived classes."""

        return ""

    def set_int_alignment(self, alignment: TextAlignment) -> None:
        """Set the text alignment of a int field."""
        self._text_alignment[IntField] = alignment

    def set_float_alignment(self, alignment: TextAlignment) -> None:
        """Set the text alignment of a float field."""
        self._text_alignment[FloatField] = alignment

    def set_string_alignment(self, alignment: TextAlignment) -> None:
        """Set the text alignment of a string field."""
        self._text_alignment[StringField] = alignment

    def generate_lines(self) -> List[str]:
        """Generate the text representation (so a sequence of lines) corresponding to this
        keyword.

        """

        def _make_line(
            fields_srep, sequence_of_fields, field_values, autofill=False, shrink=False
        ) -> str:
            """Internal utility function to avoid duplicating code."""

            index_shift = 0
            for field, value in zip(sequence_of_fields, field_values):
                if shrink:
                    size = floor(100 / len(field_values))
                    autofill = True
                else:
                    size = FIELDWIDTH * field.span

                # Get the text alignment for this particular field.
                if getattr(field, "alignment", False):
                    alignment = field.alignment
                else:
                    alignment = self._text_alignment[field.__class__]

                if alignment == TextAlignment.LEFT:
                    srep = field(value).ljust(size)
                elif alignment == TextAlignment.CENTER:
                    srep = field(value).center(size)
                else:
                    srep = field(value).rjust(size)

                fields_srep[field.index - 1 - index_shift] = srep

                index_shift += field.span - 1

            line = "".join(fields_srep)

            if autofill:
                line = line.ljust(100)

            if len(line) != 100:
                raise RuntimeError("Runtime assertion `len(line) == 100` failed (bug).")

            return line

        def _handle_atomic(lines, line_definition):
            """Internal utility function that handles atomic field definitions."""

            total_span = sum([getattr(field, "span", 1) for field in line_definition])

            if total_span > 10:
                if self.category != KeywordCategory.ENGINE:
                    raise RuntimeError(
                        "Inconsistent value for `total_span` (must be <=10). (BUG)"
                    )
                nfields = len(line_definition)
                shrink = True
            else:
                nfields = NFIELDS - total_span + len(line_definition)
                shrink = False

            fields_srep = nfields * [FIELDWIDTH * " "]

            field_values = []
            for field in line_definition:
                attr = field.attr
                if attr == "__blank__":
                    field_values.append("")
                    continue

                # This is the common case
                if ":" not in field.attr:
                    field_values.append(getattr(self, attr))
                    continue

                # In this case, the values are indices in a sequence.
                attr, index_as_str = attr.split(":")
                index = int(index_as_str)

                field_values.append(getattr(self, attr)[index])

            lines.append(
                _make_line(fields_srep, line_definition, field_values, shrink=shrink)
            )

        def _handle_array_of_atomic_fields(lines, line_definition):
            """Internal utility function that handles array of fields definitions."""

            # Initialize the fields that we need to fill
            nfields = NFIELDS - line_definition.span + len(line_definition.fields)

            # Initialize string representation of fields (field values). Note
            # that only the number of fields is important here. The size of
            # each field is obtained from the `span` attribute of the field.
            fields_srep = nfields * [FIELDWIDTH * " "]

            field_array_info = []
            # Gather information on how the column of data associated with this
            # attribute is obtained from the associated array like object.
            for field in line_definition.fields:
                # The name of the attribute referenced by this field.
                attr = field.attr

                # If this attribute references a column in a multi-column array, a colon
                # must be used to separate the label of the attribute from the index.
                ncolons = attr.count(":")

                if ncolons > 1:
                    raise RuntimeError(
                        "Attribute names can only contain a single `:` (BUG)."
                    )

                if ncolons == 0:
                    if not hasattr(self, attr):
                        raise RuntimeError(
                            f"Inconsistency detected: `{attr}` does not exist."
                        )

                    array = getattr(self, attr)

                    if hasattr(array, attr):
                        field_array_info.append(
                            ArrayInfo(attr, attr, IndexStyle.BY_NAME)
                        )
                    else:
                        field_array_info.append(ArrayInfo(attr, None, IndexStyle.NONE))

                    continue

                attr, index = attr.split(":")

                if not "|" in index:
                    raise RuntimeError(
                        "Indices must have the `<label>|<column_index>` format (BUG)."
                    )

                column_name, column_index = index.split("|")
                column_index = int(column_index)

                array = getattr(self, attr)

                if hasattr(array, column_name):
                    field_array_info.append(
                        ArrayInfo(attr, column_name, IndexStyle.BY_NAME)
                    )
                else:
                    field_array_info.append(
                        ArrayInfo(attr, column_index, IndexStyle.BY_COLUMN_INDEX)
                    )

            nrows = len(getattr(self, field_array_info[0].attr))

            # Generate a line for each row in the arrays associated to this
            # `ArrayOfAtomicFields` instance.
            for row_index in range(nrows):
                field_values = []
                for array_info in field_array_info:
                    array = getattr(self, array_info.attr)

                    if array_info.index_style == IndexStyle.NONE:
                        field_values.append(array[row_index])
                        continue

                    if array_info.index_style == IndexStyle.BY_COLUMN_INDEX:
                        field_values.append(array[row_index][array_info.column_index])
                        continue

                    if array_info.index_style == IndexStyle.BY_NAME:
                        field_values.append(array[array_info.column_index][row_index])
                        continue

                    raise RuntimeError("Invalid index style (BUG).")

                lines.append(
                    _make_line(fields_srep, line_definition.fields, field_values)
                )

        def _handle_multi_line_array_of_atomic_fields(lines, line_definition):
            """Internal utility function that handles multiple row array of
            atomic fields definitions."""

            narray_of_fields = len(line_definition.fields)

            lines_per_array_of_fields = [[] for _ in range(narray_of_fields)]

            for i, array_of_atomic_fields_obj in enumerate(line_definition.fields):
                # Delegate the work
                _handle_array_of_atomic_fields(
                    lines_per_array_of_fields[i], array_of_atomic_fields_obj
                )

            # Because of the way the work is delegated, the resulting lines are
            # not in the correct order. That is why we separated out the
            # collection of lines to separate lists. We now need to put them in
            # the correct order and add them to the global `lines` list.
            for line_group in zip(*lines_per_array_of_fields):
                lines.extend(line_group)

        def _handle_vl_sequence_of_atomic_field(lines, line_definition):
            """Internal utility function that handles definitions of variable
            length fields of the same type (e.q. the `box_id` fields in the
            /BOX/BOX keyword."""

            def _make_make_line_info(atomic_field, field_values):
                """Internal utility function to prevent code duplication."""

                # The underlying class of the field that we need to instantiate
                atomic_field_cls = atomic_field.__class__

                # Initialize string representation of fields (field values).
                # Note that only the number of fields is important here. The
                # size of each field is obtained from the `span` attribute of
                # the field.
                fields_srep = len(field_values) * [FIELDWIDTH * " "]

                # Instantiate the underlying class with the proper index.
                sequence_of_fields = []
                for i in range(len(field_values)):
                    index = i * atomic_field.span + 1
                    sequence_of_fields.append(
                        atomic_field_cls(atomic_field.attr, index)
                    )

                # Return the information we need to directly call `_make_line`
                return (fields_srep, sequence_of_fields, field_values)

            # The field obj that defines the variable length sequence of fields.
            atomic_field = line_definition.field

            # The maximum number of fields on a single line (e.g. 10 for an
            # integer field and 5 for a float field)
            max_fields_per_line = int(NFIELDS / atomic_field.span)

            # The variable length sequence of values that we need to put into
            # the keyword.
            vl_sequence_of_atomic_field_values = getattr(self, atomic_field.attr)

            # Collecting the field values per line. If a line is complete filled, we
            # create the text presentation of this line.
            field_values = []
            for field_value in vl_sequence_of_atomic_field_values:
                if len(field_values) == max_fields_per_line:
                    lines.append(
                        _make_line(*_make_make_line_info(atomic_field, field_values))
                    )
                    field_values = []

                field_values.append(field_value)

            # Don't forget the case where a line is not completely filled after
            # we are done iterating of the variable length sequence of values.
            if len(field_values) != 0:
                lines.append(
                    _make_line(
                        *_make_make_line_info(atomic_field, field_values), autofill=True
                    )
                )

        # Check pre-conditions for this keyword
        self.check_pre_conditions()

        # Initialize the list of lines that is the text representation of this
        # keyword.
        lines = [self.keyword.ljust(100)]

        # Process the fields in this keyword by looping over the structure
        # definition.
        for line_definition in self.structure:
            line_definition_type = get_line_definition_type(line_definition)

            # Dispatch to the correct handler
            match line_definition_type:

                case LineDefinitionType.SINGLE_ATOMIC_FIELD:
                    _handle_atomic(lines, [line_definition])

                case LineDefinitionType.SEQUENCE_OF_ATOMIC_FIELDS:
                    _handle_atomic(lines, line_definition)

                case LineDefinitionType.ARRAY_OF_ATOMIC_FIELDS:
                    _handle_array_of_atomic_fields(lines, line_definition)

                case LineDefinitionType.MULTI_LINE_ARRAY_OF_ATOMIC_FIELDS:
                    _handle_multi_line_array_of_atomic_fields(lines, line_definition)

                case LineDefinitionType.VL_SEQUENCE_OF_ATOMIC_FIELD:
                    _handle_vl_sequence_of_atomic_field(lines, line_definition)

                case _:
                    raise RuntimeError("No case matches line definition (BUG)")

        return lines

    def write(self, output_stream: TextIOBase):
        for line in self.generate_lines():
            output_stream.write(f"{line}\n")


if __name__ == "__main__":
    pass
