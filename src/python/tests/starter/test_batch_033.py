from pathlib import Path

from operato.keywords.starter import (
    MatLaw66,
    MatLaw68,
    MatLaw69,
    MatLaw70,
    MatLaw71,
    MatLaw72,
    MatLaw73,
    MatLaw74,
    MatLaw75,
)

# The underscore `_` is there to circumvent a pytest warning that it cannot capture
# the TestManager class.
from operato.testutil import TestManager as _TestManager

TEST_MANAGER = _TestManager(Path("./definitions"))


def test_batch_033(interactive=False):
    keywords = (
        MatLaw66,
        MatLaw68,
        MatLaw69,
        MatLaw70,
        MatLaw71,
        MatLaw72,
        MatLaw73,
        MatLaw74,
        MatLaw75,
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
    test_batch_033(interactive=True)
