"""The contract's required check: `python3 -m pytest -q` must pass.

The gate re-runs this itself before minting a receipt — a committer (human
or agent) claiming the tests pass is never the input.
"""

from app import add, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12
