from abc import abstractproperty
from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum
from io import TextIOBase
from typing import List, Literal, Sequence, Tuple, get_args, get_type_hints
from math import floor

from operato.constants import (
    FIELDWIDTH,
    FLOAT_FULL_FORMAT_SPEC,
    INT_FULL_FORMAT_SPEC,
    NFIELDS,
)


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


class KeywordType(Enum):
    """Helper enumeration in case we need to distinguish between whether or not a particular
    keyword is an engine, starter or generic keyword. Generic in this case means the keyword
    does not need special treatment.

    The reason why this enumaration is added is to gracefully handle the case where an
    engine keyword uses more than 5 float fields on a single line (e.g. `/ALE/DISP/DONEA`).
    """

    ENGINE = 1
    STARTER = 2
    GENERIC = 3


class LineDefinitionType(Enum):
    # Example: `StringField(..)`
    SINGLE_ATOMIC_FIELD = 1
    # Example: `[IntFieldi(..), FloatField(..), FloatField(..)]`
    SEQUENCE_OF_ATOMIC_FIELDS = 2
    # Example: `VLSequenceOfAtomicField(IntField(..))`
    VL_SEQUENCE_OF_ATOMIC_FIELD = 3
    # Example: `ArrayOfAtomicFields([IntField(..), FloatField(..), FloatField(..)])`
    ARRAY_OF_ATOMIC_FIELDS = 4
    # Example: `MultiLineArrayOfAttomicFields(
    #                [ArrayOfAtomicFields(..), ArrayOfAtomicFields(..)])`
    MULTI_LINE_ARRAY_OF_ATOMIC_FIELDS = 5


class TextAlignment(Enum):
    """Options for text alignment in a field."""

    LEFT = 1
    CENTER = 2
    RIGHT = 3


class IndexStyle(Enum):
    """Represents indexing style for array like parameters. The two options are
    `BY_COLUMN_INDEX` (e.g. `nodes[row_index][col_index]`)  or
    `BY_NAME` (e.g nodes["xc"][row_index].."""

    BY_COLUMN_INDEX = 1
    BY_NAME = 2


# --- Field definitions -----------------------------------------------------------------------
#
# For each of the Radioss keywords, its structure and type of each field in the
# keyword must be defined. This is done by specifying, for each keyword, a
# sequence of field types.  Each field type contains information about the
# underlying type (bool, float, int, str), where the field is located in the
# keyword and how wide the field is/can be.
#
# The following basic field types are defined:
#  1.) BoolField   : represents a single boolean
#  2.) FloatField  : represents a single float field
#  3.) IntField    : represents a single integer field
#  4.) StringField : represents a single string field
#
# In addition, there is also an aggregate field type called `ArrayOfAtomicFields`.
# The purpose of this type is to represent variable length arrays as found for
# example in the /NODE keyword.


@dataclass
class BoolField:
    """Represents a single boolean flag field in a keyword."""

    attr: str
    index: int
    nflags: int
    positions: List[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

    @property
    def span(self):
        return 1

    def __call__(self, values):
        if len(values) != self.nflags:
            raise ValueError("Condition `len(values) != nflags` is violated.")

        flags = 10 * [" "]
        for position, value in zip(self.positions, values):
            if value not in (0, 1):
                raise ValueError("Boolean values must be either 0 or 1.")

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

    field: IntField | FloatField


@dataclass
class ArrayOfAtomicFields:
    """Represents the fields in keywords that are arrays (like /NODE).

    When a field is defined inside a `ArrayOfAtomicFields` object, the `attr` argument must follow
    a particular pattern in case of a multi-dimensional array. For example, the `xc` field
    in the /NODE keyword is defined as `FloatField("xc_yc_zc:0")` where `xc_yc_zc` is the
    Nx3 Numpy array holding the coordinates and `0` is the column index of this array
    that corresponds to the `xc` coordinate.

    """

    fields: Sequence[IntField | FloatField]

    @property
    def span(self) -> int:
        return sum([field.span for field in self.fields])

    @property
    def name_column_index_style_tuples(
        self,
    ) -> List[Tuple[str, None | int | str, None | IndexStyle]]:
        name_index_tuples = []
        for field in self.fields:
            # The `attr` attribute in the initializer of a field is a string that must
            # resolve to an attribute in the corresponding keyword definition. Except for
            # an `ArrayOfAtomicFields` the `attr` must exactly match the attribute name in the
            # corresponding keyword. For an `ArrayOfAtomicFields` `attr` can be encoded in a few
            # ways:
            #   - `attr` in this case the attribute directly references a the
            #      attribute name of the corresponding keyword class
            #   - `attr:<index>` in this case, `attr` is the name of the attribute in the
            #      keyword instance and <index> is the column index
            #   - `attr:<label>` in this case, `attr` is the name of the attribute in the
            #      keyword class and <label> is the column name
            parts = field.attr.split(":")

            # The first part (part[0]) is always the name of the array like attribute in the
            # keyword class.
            attr = parts[0]
            if len(parts) == 1:
                # The array represents a single column (sequence) of values
                column = None
                index_style = None
            elif len(parts) == 2:
                # The array is multi-dimensional (multi-column) where the column we
                # need to extract the data from is given either by column index or by name.
                try:
                    # If no exception is raised, it is a column index
                    column = int(parts[1])
                    index_style = IndexStyle.BY_COLUMN_INDEX
                except ValueError:
                    # If an exception is raised, it is a column name
                    column = parts[1]
                    index_style = IndexStyle.BY_NAME
            else:
                raise RuntimeError("Error encountered while parsing `{field.attr}`.")

            name_index_tuples.append((attr, column, index_style))

        return name_index_tuples


@dataclass
class MultiLineArrayOfAtomicFields:
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
            # Note: specifying an alignment for a `BoolField` has no effect because the
            #       string representation of a `BoolField` is always exactly 10 characters
            #       (so, as wide as the field). Add it here, because it allows us to process
            #       the fields regardless of its specific type.
            BoolField: TextAlignment.CENTER,
            FloatField: TextAlignment.CENTER,
            IntField: TextAlignment.CENTER,
            StringField: TextAlignment.LEFT,
        }

        # Both starter and engine keywords can be treated in the same way if the
        # keyword type equals `KeywordType.GENERIC`. If either a starter or an engine
        # needs special treatment, use `KeywordType.STARTER` or `KeywordType.ENGINE`
        # respectively.
        self.type = KeywordType.GENERIC

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
                if self.type != KeywordType.ENGINE:
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

        def _handle_array_of_fields(lines, line_definition):
            """Internal utility function that handles array of fields definitions."""

            # Initialize the fields that we need to fill
            nfields = NFIELDS - line_definition.span + len(line_definition.fields)

            # Initialize string representation of fields (field values). Note that only the
            # number of fields is important here. The size of each field is obtained from
            # the `span` attribute of the field.
            fields_srep = nfields * [FIELDWIDTH * " "]

            # Returns a tuple of (<array name>, <column index in array name>).
            # There is one entry for each field.
            name_column_index_style_tuples = (
                line_definition.name_column_index_style_tuples
            )

            # It is implicitly assumed that the check, that all arrays referenced by
            # the fields have the same length, is done.
            nrows = len(getattr(self, name_column_index_style_tuples[0][0]))

            # Generate a line for each row in the arrays associated to this
            # `ArrayOfAtomicFields` instance.
            for row_index in range(nrows):
                field_values = []
                for name, column, index_style in name_column_index_style_tuples:
                    array = getattr(self, name)
                    if column is None:
                        value = array[row_index]
                    else:
                        if index_style == IndexStyle.BY_COLUMN_INDEX:
                            value = array[row_index][column]
                        else:
                            value = array[column][row_index]

                    field_values.append(value)

                lines.append(
                    _make_line(fields_srep, line_definition.fields, field_values)
                )

        def _handle_multi_line_array_of_fields(lines, line_definition):
            """Internal utility function that handles multiple row array of
            fields definitions."""

            # Create short-cut to keep line length within limits
            a_field = line_definition.fields[0]

            # It is implicitly assumed that the check, that all arrays referenced by
            # the fields have the same length, is done.
            nrows = len(getattr(self, a_field.name_column_index_style_tuples[0][0]))

            for row_index in range(nrows):
                for array_of_fields_obj in line_definition.fields:

                    # Initialize the fields that we need to fill
                    nfields = (
                        NFIELDS
                        - array_of_fields_obj.span
                        + len(array_of_fields_obj.fields)
                    )

                    # Initialize string representation of fields (field
                    # values). Note that only the number of fields is important
                    # here. The size of each field is obtained from the `span`
                    # attribute of the field.
                    fields_srep = nfields * [FIELDWIDTH * " "]

                    # Use the `getattr` syntax here to keep line-length within limits
                    name_column_index_style_tuples = getattr(
                        array_of_fields_obj, "name_column_index_style_tuples"
                    )
                    field_values = []
                    for name, column, index_style in name_column_index_style_tuples:
                        array = getattr(self, name)
                        if column is None:
                            value = array[row_index]
                        else:
                            if index_style == IndexStyle.BY_COLUMN_INDEX:
                                value = array[row_index][column]
                            else:
                                value = array[column][row_index]

                        field_values.append(value)

                    lines.append(
                        _make_line(
                            fields_srep, array_of_fields_obj.fields, field_values
                        )
                    )

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
                    _handle_array_of_fields(lines, line_definition)

                case LineDefinitionType.MULTI_LINE_ARRAY_OF_ATOMIC_FIELDS:
                    _handle_multi_line_array_of_fields(lines, line_definition)

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
