""""
The following example illustrates classic TDD for a standard deviation function, std().
To start, we write a test for computing the standard deviation from a list of numbers as follows
"""

from math import sqrt

#standard deviation function, std()
def std(nums):

   if len(nums) == 0: # Special case the empty list.
      return 0.0

   variance = 0.0
   
   mean =sum(nums, 0.0) / len(nums)

   for n in nums:
      variance += pow(n - mean, 2)
   
   return sqrt(variance/len(nums))

# TDD Tests -----------

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


def test_std4():
    # The first value is not zero.
    obs = std([1.0, 3.0])
    exp = 1.0
    assert obs == exp

def test_std5():
    # Here, we have more than two values, but all of the values are the same.
    obs = std([1.0, 1.0, 1.0])
    exp = 0.0
    assert obs == exp


# Run tests -----------------

# demo run of calculation
val= [12.5, 7.0, 10.0, 7.8, 15.5]
print (std(val))

# exec tests 1,2,3,4,5
test_std1() # expected 1.0
test_std2() # empty list test expected 0
test_std3() # Test a real case expected 2.0
test_std4() # value is not zero. expected 1.0
test_std5() # two same values expected 0
