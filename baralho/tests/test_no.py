import sys

sys.path.append("..\\baralho\\src")
from main import baralho2
import pytest


@pytest.mark.parametrize(
    "input, expected_result",
    [("01C02C03C04C05C07C09C10C11C02E02E03E11U", [4, "erro", 12, 13])],
)
def test_invalid(input, expected_result):
    actual = baralho2(input)
    assert actual == expected_result
