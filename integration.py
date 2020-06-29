
"""
Integration tests are the class of tests that verify that multiple moving pieces and gears inside the clock work well together. 
Where unit tests investigate the gears, integration tests look at the position of the hands to determine if the clock can tell time correctly. 
They look at the system as a whole or at its subsystems. Integration tests typically function at a higher level conceptually than unit tests. 
Thus, writing integration tests also happens at a higher level.
"""


def a(x):
    return x + 1


def b(x):
    return 2 * x


def c(x):
    return b(a(x))


assert a(1) == 2
assert b(2) == 4
assert c(2) == 6


def test_c():  # integration test
    exp = 6
    obs = c(2)
    assert obs == exp , "Integration test: Fail"
    print("Integration test: pass")

test_c()

