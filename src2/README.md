# **Part 2 - ESP8266 Simple Testing with examples in Micropython**


First part of this tutorial was covering intro and testing examples if you are interested please [read more on Part 1 link](/src1/README.md)

Some summary from part 1 of this tutorial is about what could be considered and can make sense in your case if you develop IoT application with ESP8266 and Micropython


![No Tests](/img/tests.jpg)


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

# Next steps

In third part of this tutorial I will cover complex testing scenario and untouched related topics

# Resources

Further reading and useful links:
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