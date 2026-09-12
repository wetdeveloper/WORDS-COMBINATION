from app.services.generator.generator import generate
from app.services.generator.modes import GenerationMode


def test_permutation_repeat():

    result = list(
        generate(
            ["a", "b", "c"],
            2,
            GenerationMode.PERMUTATION_REPEAT
        )
    )

    assert len(result) == 9

    assert "aa" in result
    assert "cc" in result



def test_permutation_no_repeat():

    result = list(
        generate(
            ["a", "b", "c"],
            2,
            GenerationMode.PERMUTATION_NO_REPEAT
        )
    )

    assert len(result) == 6



def test_combination_repeat():

    result = list(
        generate(
            ["a", "b", "c"],
            2,
            GenerationMode.COMBINATION_REPEAT
        )
    )

    assert result == [
        "aa",
        "ab",
        "ac",
        "bb",
        "bc",
        "cc"
    ]



def test_combination_no_repeat():

    result = list(
        generate(
            ["a", "b", "c"],
            2,
            GenerationMode.COMBINATION_NO_REPEAT
        )
    )

    assert result == [
        "ab",
        "ac",
        "bc"
    ]
