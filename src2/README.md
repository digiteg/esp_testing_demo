# **Part 2 - ESP8266 Simple Testing with examples in Micropython**


First part of this tutorial was covering intro and testing examples if you are interested please [read more on Part 1 link](/src1/README.md)

Some summary from part 1 of this tutorial is about what could be considered and can make sense in your case if you develop IoT application with ESP8266 and Micropython





## **Short recap..**


### **Best practices for effective IoT Testing**

- Gray Box testing as it allows to design effective test case
- Gray Box allows you to know the OS, the architecture, third-party hardware, new connectivity and hardware device limitation.
- Real Time Operating System
- IoT Testing should be automated


### **Challenges of IOT Testing**
- Network and internal communication
- Security
- The system complexity & bugs present in the IOT technology
- Limitations in memory, processing power, bandwidth, battery life, etc.

<br/>

# Things used in this project




 ![NodeMCU ESP8266](/img/ESP8266.jpg)

### **Hardware components**
- Waveshare NodeMCU-32S ESP32 WiFi + Bluetooth

### **Software apps and online services**
- [Thony](https://thonny.org/)
- [MicroPython unicorn online editor](https://micropython.org/unicorn/)

<br/>


# Test Driven Development

The simple concept of TDD is to write and correct the failed tests before writing new code (before development). This helps to avoid duplication of code as we write a small amount of code at a time in order to pass tests. (Tests are nothing but requirement conditions that we need to test to fulfill them).
![Test Driven Development](/img/tdd.png)

## TDD way of coding

Write unit tests at the same time as writing your the software.
Don’t waste time writing brittle tests for tests’ sake, write tests to help verify your work is correct.
The main benefit is not the regression test, it is the ensuring of good software design. 

**Best practice:**
- write failing test 
- write code
- ensure test passes
- refactor and change design
- ensure all tests pass

Adherence to these principles helps allow for incremental architecture, because tests ensure software quality at the source.
- Well-designed software is modular. 
- Independently testable code is already proven to be sufficiently independent and well-designed to allow for future redesign!


![Test Driven Development](/img/tddchuck.jpg)

# TDD showcase

The following example illustrates classic TDD for a standard deviation function, std().
To start, we write a test for computing the standard deviation from a list of numbers as follows


## Step 1: write test for proof


```python

# first test for std()
def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert obs == exp
```

## Step 2. Ensure test fails

```python
# exec test
test_std1()
```

## Step 3: Implement logic

```python
# write first implementation of standard deviation function, std()
def std(vals):
    # surely this is cheating...
    return 1.0
```

## Step 4. Ensure tests pass
```python
# exec again test
test_std1()
```

## Step 5: Write second version of standard deviation function, std()

```python
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
```
<br/>

![Test Driven Development](/img/tddfails.jpg)

## Step 6: Final implementation of standard deviation function, *std()*

```python
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
```




# Integration Test - Example

Integration tests verify multiple parts of the system. They look at the system as a whole or at its subsystems. Integration tests typically function at a higher level conceptually than unit tests. Thus, writing integration tests also happens at a higher level. For example in case of testing clock. Integration tests are the class of tests that verify that multiple moving pieces and gears inside the clock work well together. Where unit tests investigate the gears, integration tests look at the position of the hands to determine if the clock can tell time correctly. 


```python
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
```
<br/>

# Basics of testing framework

Usual vocabulary around testing frameworks contain following terms: 

**_Test case_**: test case is the smallest unit of testing. It checks for a specific response for a specific set of input data.

**_Test suite_**: test suite is a collection of test cases. It is used to aggregate tests that must be run together.

**_Test fixture_**: test fixture is the fixed state of the objects used as the source when performing tests.
- The purpose of using fixture is if you have a complex test case, then preparing the desired state can easily take a lot of resources (for example, you consider a function with certain accuracy and each next sign of accuracy in the calculations takes a day). 
- Using fixture (on slang - fixtures), we skip the preliminary preparation of the state and immediately begin testing. 
- Test fixture can appear, for example, in the form (database state, set of environment variables, set of files with the necessary content).

**_Test runner_**: test runner is a component that organizes the execution of tests and provides the result to the user.

# Basic overview 
Different libraries and frameworks for unit testing on Python:
- **Unittest** - The most popular library for unit testing in Python 
- **PyTest**  - is an open-source Python-based testing framework. It is designed for all-purpose testing and has the capability for Functional and API testing
- **Robot** - The Robot framework is also used for Robotic Process Automation (RPA).
- **Django** - allows writing automated testing for modern web development. 
- **Flask** - provides ample opportunity to test your web application using tests and by processing local context variables.

## Why to start your first steps with PyTest ?
- More pythonic way of writing your tests.
- Supports simple or complex code to test API, databases, and UIs.
- Has a Simple python syntax.
- Number of plugins.
- Ability to run tests in parallel.
- Ability to run selected specific subset of tests.


```python
# test_with_pytest

def test_always_passes():
    assert True

def test_always_fails():
    assert False
```
Execution result in following output:

```
pytest test_demo1.py
================== test session starts ======================
platform win32 -- Python 3.8.1, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: C:\Python\esp_testing_demo\src2
collected 2 items
test_demo1.py .F
					[100%]

=================== FAILURES ===================
____________________ test_always_fails ____________________
    def test_always_fails():
>       assert False
E       assert False

test_demo1.py:7: AssertionError
==================== short test summary info ====================
FAILED test_demo1.py::test_always_fails - assert False
==================== 1 failed, 1 passed in 0.12s ====================
```

Another example of Fixtures application:

```python
# pytest fixtures demo
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input


def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
```

<br/>

# MicroTest framework

My motivation do developed MicroTest framework is current challenges for development and testing on Microcontrollers like:

- Standard MicroPython testing library ?
- Manual testing for Complex projects ?
- Automated testing ?
- Effective Mockups ?

### Basic sample shows how to run your first tests with MicroTest framework. 

- **Test suite:** for us  is a collection of test cases e.q. python functions. It is used to aggregate tests that must be run together. for example in (test_wallet.py) imported in example

- **Test runner:** is class (MicroTestRunner) which organizes the execution of tests and provides the result to the user. Usage of runner is described in main() function

```python
# MicroTest demo
from microtest.microtestrunner import MicroTestRunner

# uncomment for loading more test suites into demo 
import test_wallet
#import test_fibonacci
#import test_fixture1

def main():
    runner = MicroTestRunner(globals())
    runner.exec()

if __name__ == "__main__":
    main()
```



### Execution will create following output on console and to file

```
======================= Test suite Start: test_wallet ===============================
Loaded file: c:\Python\esp_testing_demo\src2\test_wallet.py
Tests collected: 5

PASSED: test_default_initial_amount
PASSED: test_setting_initial_amount
PASSED: test_wallet_add_cash
PASSED: test_wallet_spend_cash
ERROR: test_wallet_spend_cash_raises_exception_on_insufficient_amount raised <class 'wallet.InsufficientAmount'> (None): Not enough available to spend 100

======================= Summary of: test_wallet ===============================

Total Passed 4
Total Skipped 0
Total Failed 0
Total Errors 1
Expected Failures 0
Unexpected Passes 0

```


## MicroTest - Log

MicrotTest provides built in logger for simplified output management, basic options are writing messages into file or print on console.


```python
# MicroLogger example

from microtest.micrologger import MicroLogger
from microtest.basiclogger import LogLevels

log = MicroLogger()

log.basicConfig(vlevel=LogLevels.DEBUG)
log.log_debug("Test message: {}({})", 100, "foobar")
log.log_info("Test message2: {}({})", 200, "foobar")
log.log_warning("Test message3: {}({})",300,"foobar")
log.log_error("Test message4")
log.log_critical("Test message5")
log.log_info("Test message6")

```
### Execution of script above results into following output on console and to file

```
DEBUG: Test message: 100(foobar)
INFO: Test message2: 200(foobar)
WARNING: Test message3: 300(foobar)
ERROR: Test message4
CRITICAL: Test message5
INFO: Test message6
```

# Fixtures

MicrotTest provides built in support for Fixtures - for handling test dependencies, state, and reusable functionality

- Fixtures are a way of providing data, test doubles, or state setup to your tests. 
- Fixtures are functions that can return a wide range of values. 
- Each test that depends on a fixture must explicitly accept that fixture as an argument.


```python
# Fixture example

from microtest.microtestrunner import fixture, skip, skipif, xfail, parametrize

@fixture
def input_value():
   input = 39
   return input

@fixture
def input_value2():
   input = 39
   return input

def test_divisible_by_3(input_value,input_value2 ):
   assert input_value % 3 == 0
   assert input_value2 % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
```
Another example of using Fixtures for more complex data

```python
# Fixture example 2

@fixture
def people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        }
    ]

# test data format
def test_format_data_for_display(people_data):
    assert people_data == valid_data()
```

### Execution of scripts above results into following output on console and to file

```
======================= Test suite Start: test_fixture1 ===============================
Loaded file: c:\Python\esp_testing_demo\src2\test_fixture1.py
Tests collected: 4

PASSED: test_divisible_by_3
FAILED: test_divisible_by_6 raised <class 'AssertionError'> (Assertion failed.)
PASSED: test_format_data_for_display
PASSED: test_format_data_for_excel

======================= Summary of: test_fixture1 ===============================

Total Passed 3
Total Skipped 0
Total Failed 1
Total Errors 0
Expected Failures 0
Unexpected Passes 0
```

# Marks

Additional Marks can be used apply meta data to test functions (but not fixtures), which can then be accessed by other fixtures or plugins etc.

MicroTest provides a few additional marks out of the box:
- *skip* skips a test unconditionally.

- *skipif* skips a test if the expression passed to it evaluates to True.

- *xfail* indicates that a test is expected to fail, so if the test does fail, the overall suite can still result in a passing status.

- *parametrize* (note the spelling) creates multiple variants of a test with different values as arguments. You’ll learn more about this mark shortly.

```python
# MicroTest Marks example
#--------SKIP IF----------------------------

@skipif(sys.platform == 'win32',"does not run on windows")
def test_skipif1():
    assert 0                  

#----------XFAIL --------------------------

@xfail
def test_hello():
    assert 0, "xfail"

@xfail(False)
def test_hello2():
    assert 0, "xfail 2"
```

# Parametrization: Combining Tests

In these cases, you can parametrize a single test definition, and MicroTest will create variants of the test for you with the parameters you specify.

```python
# MicroTest Parametrization example

#----------PARAMETRIZED --------------------------

testdata = [(datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
            (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
            ]


@parametrize(testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    #print("Test: {} - {} = {}".format(a, b, diff))
    assert diff == expected
```
# Approx

Assert that two numbers  are equal to each other within some tolerance.

```python
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


def main():
    test_approx0()
    test_approx_edge1()
    test_approx_internal21()
    test_approx_internalFloat()

if __name__ == "__main__":
    main()
```


# Next steps

In third part of this tutorial I will cover complex testing scenario and untouched related topics

# Resources

Further reading and useful links:
- [RealPython](https://realpython.com/pytest-python-testing/)
- [Guru99](https://www.guru99.com/software-testing.html)
- [Software Testing Help](https://www.softwaretestinghelp.com/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)
- [wikipedia Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number)
- [wikipedia Standard deviation](https://en.wikipedia.org/wiki/Standard_deviation)


# Credits


# License
Unless otherwise noted, the contents of this document are licensed under a license
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

![Creative Commons](/img/cc.svg) ![by](/img/by.svg) ![nc-eu](/img/nc-eu.svg) ![sa](/img/sa.svg)