
"""
Integration tests verify multiple parts of the system. 
They look at the system as a whole or at its subsystems. 
Integration tests typically function at a higher level conceptually than unit tests. 
Thus, writing integration tests also happens at a higher level. 
For example in case of testing clock. Integration tests are the class of tests that verify that multiple moving pieces and gears inside the clock work well together. 
Where unit tests investigate the gears, integration tests look at the position of the hands to determine if the clock can tell time correctly. 
"""


# Simple Integration tests example  

def add_one(x): 
    return x + 1


def multiply_by2(x):
    return 2 * x


def add_one_and_multiply_by2(x):
    return multiply_by2(add_one(x))

# test the logic

assert add_one(1) == 2
assert multiply_by2(2) == 4
assert add_one_and_multiply_by2(2) == 6

# Integration test --------

def test_integration():  
    exp = 6
    obs = add_one_and_multiply_by2(2)
    assert obs == exp , "Integration test: Fail"
    print("Integration test: pass")

# Exec integration test
test_integration()
