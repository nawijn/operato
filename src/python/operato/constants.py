from typing import Literal

# A single `line` in a (starter) keyword by definition consists of 10 fields
# each 10 characters long. As a consequence, the maximum number of characters
# on a single line is 100. A particular value that must be stored in a keyword,
# can span 1 or more fields. In particular, `bool` and `int` logical fields
# span a single physical field; a `float` logical field spans 2 physical fields
# and a `string` logical field spans 1 to 10 physical fields depending on the
# context.

# The width in characters within a single (physical) field.
FIELDWIDTH = 10

# The maximum number of physical fields in a single line.
NFIELDS = 10

# Although OpenRadioss supports both textual as numerical specifiers for mass,
# length and time units, it is highly recommended (and currently the only
# supported way) to use the textual one.
VALID_MASS_LITERALS = Literal[
    "yg",
    "zg",
    "ag",
    "fg",
    "pg",
    "ng",
    "mug",
    "mg",
    "cg",
    "dg",
    "g",
    "dag",
    "hg",
    "kg",
    "Mg",
    "Gg",
    "Tg",
    "Pg",
    "Eg",
    "Zg",
    "Yg",
]

VALID_LENGTH_LITERALS = Literal[
    "ym",
    "zm",
    "am",
    "fm",
    "pm",
    "nm",
    "mum",
    "mm",
    "cm",
    "dm",
    "m",
    "dam",
    "hm",
    "km",
    "Mm",
    "Gm",
    "Tm",
    "Pm",
    "Em",
    "Zm",
    "Ym",
]

VALID_TIME_LITERALS = Literal[
    "ys",
    "zs",
    "as",
    "fs",
    "ps",
    "ns",
    "mus",
    "ms",
    "cs",
    "ds",
    "s",
    "das",
    "hs",
    "ks",
    "Ms",
    "Gs",
    "Ts",
    "Ps",
    "Es",
    "Zs",
    "Ys",
]

# The default format strings for float's and int's.
FLOAT_FORMAT = ":G"
INT_FORMAT = ":d"

# Full string specification for use with `f`-strings.
FLOAT_FULL_FORMAT_SPEC = f"{{value{FLOAT_FORMAT}}}"
INT_FULL_FORMAT_SPEC = f"{{value{INT_FORMAT}}}"

# Line separator that can be used for debugging or when more verbose output is
# desired.
LINE_SEPARATOR = ["#--------]"]
LINE_SEPARATOR.extend(9 * ["[--------]"])
LINE_SEPARATOR = "".join(LINE_SEPARATOR)
