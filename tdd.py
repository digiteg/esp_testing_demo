""""
The following example illustrates classic TDD for a standard deviation function, std().
To start, we write a test for computing the standard deviation from a list of numbers as follows
"""


# (1) -----------

def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert obs == exp


# (2) ------------------



def std(vals):
    # surely this is cheating...
    return 1.0


# (3) -----------------

def std(vals):
    # a little better
    if len(vals) == 0: # Special case the empty list.
        return 0.0
    return vals[-1] / 2.0 # By being clever, we can get away without doing real work.




# (3) -----------
def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert obs == exp


def test_std2():
    # Test the fiducial case when we pass in an empty list.
    obs = std([])
    exp = 0.0
    assert obs == exp


def test_std3():
    # Test a real case where the answer is not one.
    obs = std([0.0, 4.0])
    exp = 2.0
    assert obs == exp

# (1) -----------------
test_std1()

# (3) -----------------
test_std1()
test_std2()
test_std3()





