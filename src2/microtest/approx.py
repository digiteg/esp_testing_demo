DEFAULT_ABSOLUTE_TOLERANCE = 1e-12  # type: Union[float, Decimal]
DEFAULT_RELATIVE_TOLERANCE = 1e-6  # type: Union[float, Decimal]


def approx(actual, expected, abst=None, relt=None):

    def set_default(x, default):
        return x if x is not None else default

    absolute_tolerance = set_default(abst, DEFAULT_ABSOLUTE_TOLERANCE)
    relative_tolerance = set_default(
        relt, DEFAULT_RELATIVE_TOLERANCE) * abs(expected)
    # Return the larger of the relative and absolute tolerances.

    tolval = max(relative_tolerance, absolute_tolerance)
    return abs(expected - actual) <= tolval

 #  Boundary Values technique


def test_approx0():
    assert approx(0, 0, 0, 0) == True  # test edge 0


def test_approx_edge1():
    assert approx(0, 1, 1, 1) == True   # test edge 1


def test_fib_internal21():
    assert approx(2, 1, 3, 3) == True  # test internal point expected 21


def test_fib_internalFloat():
    assert approx(3.1934, 3.2, 0.01) == True  # test internal point expected 21


test_approx0()
test_approx_edge1()
test_fib_internal21()
test_fib_internalFloat()
