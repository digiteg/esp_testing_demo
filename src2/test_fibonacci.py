from fibonacci import fib

 #  Boundary Values technique
def test_fib_edge0():
    assert fib(0) == 0  # test edge 0

def test_fib_edge1():
    assert fib(1) == 1   # test edge 1

def test_fib_internal21():
    assert fib(8) == 21  # test internal point expected 21

    #  Error Guessing technique
def test_fib_invalid_minus1():
    assert fib(-1) == 1, "invalid value -1"  # test invalid value

def test_fib_invalid_none():
    assert fib(None) == 0, "invalid value None"  # test null value

def test_fib_invalid_string():
    assert fib('a') == 0, "invalid value 'a'"  # test wrong value type

