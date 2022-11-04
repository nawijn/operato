from pathlib import Path

from operato.keywords.engine import (
    DtTherm,
    Dt1BrickKeyword3Iflag,
    Dt1Shell,
    Dt1tet10,
    Dtix,
    Dtsde,
    Dttsh,
    DynainDt,
    DynainShellStrainFull,
)

# The underscore `_` is there to circumvent a pytest warning that it cannot capture
# the TestManager class.
from operato.testutil import TestManager as _TestManager

TEST_MANAGER = _TestManager(Path("./definitions"))


def test_batch_009(interactive=False):
    keywords = (
        DtTherm,
        Dt1BrickKeyword3Iflag,
        Dt1Shell,
        Dt1tet10,
        Dtix,
        Dtsde,
        Dttsh,
        DynainDt,
        DynainShellStrainFull,
    )

    missing_keyword_definition_files = 0

    for keyword in keywords:
        TEST_MANAGER.set_keyword_class(keyword)
        try:
            TEST_MANAGER.load_keyword_definition()
        except FileNotFoundError:
            missing_keyword_definition_files += 1
            continue

        if interactive:
            TEST_MANAGER.show_keyword()
        else:
            TEST_MANAGER.test_keyword()

        TEST_MANAGER.reset()

    if missing_keyword_definition_files > 0:
        print(
            f"{missing_keyword_definition_files} keyword definition files were missing."
        )


if __name__ == "__main__":
    test_batch_009(interactive=True)
