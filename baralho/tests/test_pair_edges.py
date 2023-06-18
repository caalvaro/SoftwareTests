import sys

sys.path.append("..\\baralho\\src")
from main import baralho2
import pytest


@pytest.mark.parametrize(
    "input, expected_result",
    [("", [13, 13, 13, 13])],
)
def test_invalid(input, expected_result):
    actual = baralho2(input)
    assert actual == expected_result
