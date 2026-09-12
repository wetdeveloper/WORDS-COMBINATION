from math import factorial



def permutation_repeat(
    elements_count,
    length
):

    return elements_count ** length



def permutation_no_repeat(
    elements_count,
    length
):

    if length > elements_count:
        return 0

    return (
        factorial(elements_count)
        //
        factorial(elements_count - length)
    )



def combination_no_repeat(
    elements_count,
    length
):

    if length > elements_count:
        return 0

    return (
        factorial(elements_count)
        //
        (
            factorial(length)
            *
            factorial(elements_count - length)
        )
    )



def combination_repeat(
    elements_count,
    length
):

    return (
        factorial(
            elements_count + length - 1
        )
        //
        (
            factorial(length)
            *
            factorial(elements_count - 1)
        )
    )
