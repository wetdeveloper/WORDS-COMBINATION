from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
)

from .modes import GenerationMode



def generate(elements, length, mode):

    if mode == GenerationMode.PERMUTATION_REPEAT:

        yield from (
            "".join(item)
            for item in product(
                elements,
                repeat=length
            )
        )


    elif mode == GenerationMode.PERMUTATION_NO_REPEAT:

        yield from (
            "".join(item)
            for item in permutations(
                elements,
                length
            )
        )


    elif mode == GenerationMode.COMBINATION_REPEAT:

        yield from (
            "".join(item)
            for item in combinations_with_replacement(
                elements,
                length
            )
        )


    elif mode == GenerationMode.COMBINATION_NO_REPEAT:

        yield from (
            "".join(item)
            for item in combinations(
                elements,
                length
            )
        )


    else:

        raise ValueError(
            "Unknown generation mode"
        )
