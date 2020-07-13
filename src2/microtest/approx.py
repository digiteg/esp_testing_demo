DEFAULT_ABSOLUTE_TOLERANCE = 1e-12  # type: Union[float, Decimal]
DEFAULT_RELATIVE_TOLERANCE = 1e-6  # type: Union[float, Decimal]


def set_default(x, default):
    return x if x is not None else default


def approx(actual, expected, abst, relt):
    absolute_tolerance = set_default(abst, DEFAULT_ABSOLUTE_TOLERANCE)
    relative_tolerance = set_default(
        relt, DEFAULT_RELATIVE_TOLERANCE) * abs(expected)
    # Return the larger of the relative and absolute tolerances.

    tolval = max(relative_tolerance, absolute_tolerance)
    return abs(expected - actual) <= tolval



