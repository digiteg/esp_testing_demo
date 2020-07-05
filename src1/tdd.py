# The following example illustrates classic TDD for a standard deviation function, std().
# To start, we write a test for computing the standard deviation from a list of numbers as follows


## -------------- Step 1: write test for proof

# first test for std()
def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert obs == exp

##--------------- Step 2: Ensure test fails

# exec test
test_std1()

## -------------- Step 3: Implement logic

# write first implementation of standard deviation function, std()
def std(vals):
    # surely this is cheating...
    return 1.0

## -------------- Step 4: Ensure tests pass

# exec again test
test_std1()


#-------------
#
## -------------- Step 5: Write second version of standard deviation function, std()
#
#-------------


# second version of standard deviation function, std()
def std(vals):
    # a little better
    if len(vals) == 0: # Special case the empty list.
        return 0.0
    return vals[-1] / 2.0 # By being clever, we can get away without doing real work.

# TDD Tests -----------

# add more tests 
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

# Run tests -----------------

# exec tests 1,2,3
test_std1() # expected 1.0
test_std2() # empty list test expected 0
test_std3() # Test a real case expected 2.0
