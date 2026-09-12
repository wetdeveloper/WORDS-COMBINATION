from app.services.generator.counter import (
    permutation_repeat,
    permutation_no_repeat,
    combination_no_repeat,
    combination_repeat,
)


def test_permutation_repeat_count():

    assert permutation_repeat(3, 5) == 243



def test_permutation_no_repeat_count():

    assert permutation_no_repeat(5, 3) == 60



def test_combination_no_repeat_count():

    assert combination_no_repeat(5, 3) == 10



def test_combination_repeat_count():

    assert combination_repeat(3, 2) == 6
