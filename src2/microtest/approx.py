DEFAULT_ABSOLUTE_TOLERANCE = 1e-12  # type: Union[float, Decimal]
DEFAULT_RELATIVE_TOLERANCE = 1e-6  # type: Union[float, Decimal]

""""
Multiplication Factors	                        Prefix	Symbol
1E+24	1,000,000,000,000,000,000,000,000	    yotta	Y
1E+21	1,000,000,000,000,000,000,000	        zetta	Z
1E+18	1,000,000,000,000,000,000	            exa	E
1E+15	1,000,000,000,000,000	                peta	P
1E+12	1,000,000,000,000	                    tera	T
1E+9	1,000,000,000	                        giga	G
1E+6	1,000,000	                            mega	M
1E+3	1,000	                                kilo	k
1E+2	100	                                    hecto	h
1E+1	10	                                    deka	da
1E+0	1	                                    -	    -
1E-1	0.1	                                    deci	d
1E-2	0.01	                                centi	c
1E-3	0.001	                                milli	m
1E-6	0.000 001	                            micro	µ
1E-9	0.000 000 001	                        nano	n
1E-12	0.000 000 000 001	                    pico	p
1E-15	0.000 000 000 000 001	                femto	f
1E-18	0.000 000 000 000 000 001	            atto	a
1E-21	0.000 000 000 000 000 000 001	        zepto	z
1E-24	0.000 000 000 000 000 000 000 001	    yocto	
"""



def approx(actual, expected, abst=None, relt=None):

    def _set_value_default(x, default):
        return x if x is not None else default

    absolute_tolerance = _set_value_default(abst, DEFAULT_ABSOLUTE_TOLERANCE)
    relative_tolerance = _set_value_default(relt, DEFAULT_RELATIVE_TOLERANCE) * abs(expected)

    # Return the larger of the relative and absolute tolerances.

    tolval = max(relative_tolerance, absolute_tolerance)
    return abs(expected - actual) <= tolval

 #  Boundary Values technique


def test_approx0():
    assert approx(0, 0, 0, 0) == True  # test edge 0


def test_approx_edge1():
    assert approx(0, 1, 1, 1) == True   # test edge 1


def test_approx_internal21():
    assert approx(2, 1, 3, 3) == True  # test internal point expected 21


def test_approx_internalFloat():
    assert approx(3.1934, 3.2, 0.01) == True  # test internal point expected 21


test_approx0()
test_approx_edge1()
test_approx_internal21()
test_approx_internalFloat()
