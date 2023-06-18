from baralho.src.main import baralho2


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ([1, [(0, 10), (0, 10), (1, 10), (2, 10), (30, 10)]], 1),
        ([1, [(0, 25), (0, 25), (0, 25)]], 2),
        ([1, [(0, 20), (0, 25), (0, 25), (0, 25)]], 2),
        ([1, [(0, 21), (0, 25), (0, 25)]], 2),
        ([2, [(0, 35), (5, 35), (10, 20)]], 1),
    ],
)
def test_invalid(input, expected_result):
    actual = baralho2(*input)
    assert actual == expected_result
