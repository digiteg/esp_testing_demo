from math import sqrt

""""
The following example illustrates classic TDD for a standard deviation function, std().
To start, we write a test for computing the standard deviation from a list of numbers as follows
"""


# (4) -----------------

def std(nums):

   if len(nums) == 0: # Special case the empty list.
      return 0.0

   variance = 0.0
   
   mean =sum(nums, 0.0) / len(nums)

   for n in nums:
      variance += pow(n - mean, 2)
   
   return sqrt(variance/len(nums))

# (4) -----------
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


# (4) -----------------

val= [12.5, 7.0, 10.0, 7.8, 15.5]
print (std(val))

test_std1()
test_std2()
test_std3()
test_std4()
test_std5()
