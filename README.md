# **ESP8266 Simple Testing with examples in Micropython**

I was digging on internet for some examples about testing on ESP8266 in Micropython just for myself education purpose and I didn't find too much useful examples for me. So I decided to fill this gap and I hope this can be  also useful for others who are willing to deal with the topic or teach their students about basics and how to automate testing. Why ESP8266 ? Because it is cost-effective and highly integrated Wi-Fi MCU for IoT / smart things... applications




<br/>

# Things used in this project




 ![NodeMCU ESP8266](/img/ESP8266.jpg)

### **Hardware components**
- NodeMCU ESP8266

### **Software apps and online services**
- Thony

<br/>

# Long story short

![Testing Phase](/img/introtesting.png)

## **Back to Testing..**

You can find lot of great articles about this topic explaining why it is worth spend so much time with Testing or why TDD make sense and so on. Usually my first and simple answer why is ist just because we want to suppress future costs of fixing bugs in production. Real nightmare of each developer doing coding for living should be spending hours of life time in finding bugs in code done by someone else running production with help of neurotic manager who is keeping him or her in pace..  
 
Some summary from my small internet research is bellow and it is about what could be considered and make sense in our case if we develop IoT application with ESP8266 and Micropython

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

# PRINCIPLES OF TESTING

There are many different types of testing that you can use to make sure that changes to your code are working as expected.
At a high level, Manual testing is done in person, for example by pushing buttons observing LEDs or interacting with APIs etc. Automated tests, are performed by a machine that executes a test script that has been written for our case in MicroPython.

![Types of Testing](/img/typestesting.png)

#### White Box testing
White-box testing is a testing technique which checks the internal functioning of the system. The white-box Testing method assumes that the Tester knows the code logic in a unit or program etc.

#### Black Box testing
Black-box testing, a tester doesn't have any information about the internal working of an application. Black box testing is a high level of testing that focuses on the behavior and involves testing from an external or end-user perspective. Black box testing can be applied to virtually every level of software testing: unit, integration, system, and acceptance...



#### Functional tests
Functional testing is a type of testing which verifies that each function of an application operates in conformance with the requirement specification. They only verify the output of an action and do not check the intermediate states of the system when performing that action.

#### Unit tests
Unit tests are very low level. They consist in testing individual methods of the classes and functions and are in general quite cheap to automate and can be run very quickly in continuous integration scenarios.This is done by developer usually.

#### Integration tests
Integration testing is a bottom-up approach for testing when new functionality is added new test are created. Application functionality and modules should be independent enough to be tested separately. This is done by developer usually or by tester.


#### Non-Functional tests
Non-functional testing is a type of testing to check non-functional aspects (compatibility, performance, usability,  etc.) of an application. It is explicitly designed to test the readiness of a system as per nonfunctional parameters which are never addressed by functional testing.

<br/>

# Let's start with first level

Unit Tests are just functions ...
- **Unit tests** are typically made of three pieces, some **setup**, a number of **assertions**, and some **tear-down**. 

- **Setup** can be as simple as initializing the input values or as complex as creating and initializing concrete instances of a class. 

- **Execution**, the test occurs when an assertion is made, comparing the observed and expected values. For example, let us test  that our mean function successfully calculates the known value for a simple list.

Try to copy and paste following code examples into REPL

## Step 1: MicroPython hello _**assert**_ Keyword

The assert keyword is usually used when we debugging or and lets you test if a condition in your code returns *True*, if not, the program will raise an *AssertionError*.
You can also add a message to be written if the code returns False, check the examples below.

```python
x = "hello Micropython"
    
#if condition returns True, then nothing happens:
assert x == "hello Micropython"
    
#if condition returns False, AssertionError is raised:
assert x == "bye"
```
## Step 2:  Add message

Write a message if the condition is False

```python
x = "hello Micropython"

#if condition returns False, AssertionError is raised:

assert x == "bye", "x should be 'hello Micropython'"
```
## Step 3: Handle *AssertionError* exceptions with  _**try**_ / _**except**_ / _**finally**_ block

In example the try block raises an *AssertionError* and the except block will be executed. Without the try block, program will crash and raise an error

```python
# try/except/finally example

try:
    assert "Hello" == "Hello"
    assert 3 == 2, "Failed"
    print("Test try/except/finally : pass")

except AssertionError as err:
    print("Test try/except/finally Assertion error: {0}".format(err))
except:
    print("An unexpected exception occurred")
finally:
    print("Teardown try/except/finally...")
```

## Step 4: *Array* example

```python
# Array Test:

test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]

assert test_list1 == test_list2
print("Array test : pass")
```
## Step 5: *Tuple* example

```python
# Tuple Test:

test_tuple1 = ("apple", "banana", "cherry")
test_tuple2 = ("apple", "banana", "cherry")

assert test_tuple1 == test_tuple2
print("Tuple test : pass")
```
## Step 6: *Set* example

```python
# Set test

test_set1 = {"apple", "banana", "cherry"}
test_set2 = {"apple", "banana", "cherry"}

assert test_set1 == test_set2
print("Set test: pass")
```
## Step 7: *Dictionary* example

```python
# Dictionary test:

test_dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

test_dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

assert test_dict1 == test_dict2
print("Dictionary test: pass")
```

<br/>

# Testing Techniques 
Idea of Testing Techniques is to help you to design better test cases. In this part of tutorial you will learn about 7  testing techniques.

## 1. Equivalence Partitioning

The aim of this testing is to remove redundant test cases within a specific group which generates the same output but not any defect. The concept itself is that we consider test a representative value of each class equal to a test of any other value of the same class. It allows you to identify valid as well as invalid equivalence classes.

![Equivalence Partitioning](/img/testtecheqp.png)


```python
# Equivalence Partitioning

age = 18  # entered age

"""
age = 5
age = 17
age = 18
age = 30
age = 59
age = 61

age = -1
age = 0
age = None
"""


assert age >= 18 and age <= 60, "Equivalence Partitioning test Fail: <=17 Invalid, 18-60 valid, >=61 Invalid"
print("Equivalence Partitioning test: pass")
```

## 2. Boundary Value Analysis

This type of testing checks the behavior of the application at the boundary level. It includes maximum, minimum, inside or outside boundaries, typical values and error values.


![Boundary Value Analysis](/img/testtechbva.png)


```python
# Boundary Value Analysis


def validateAge(age):
    return (age >= 18) and (age <= 60)


def testBVA():
    age_min = 17
    age_max = 60

    min_0 = age_min - 1
    min_1 = age_min + 1
    min_m = age_min + age_max / 2
    max_1 = age_max
    max_2 = age_max + 1

    def inner(age):
        assert validateAge(
            age), "Boundary Value Analysis test Fail: <=17 Invalid, 18-60 valid, >=61 Invalid"

    inner(18)

#    inner(min_0)
#    inner(min_1)
#    inner(min_m)
#    inner(max_1)
#    inner(max_2)

    print("Boundary Value Analysis test: pass")


testBVA()
```

<br/>

## 3. Decision Table Testing

A decision table is also known as to Cause-Effect table. This testing technique is used for functions which respond to a combination of inputs or events. Following example covers 3 clearly distinguished printer issues with how to fix them actions translated into **Decision table**

### **Printer issues - Decision Table / Cause-Effect**
|Conditions|Rule 1|Rule 2|Rule 3|Rule 4|Rule 5|Rule 6| Rule 7|
| :----------------|---:|---:| ----:| ----:| ----:|----:|----:|
| Printer does not print | True	 | True | False | False | True | True | False
| A red light is flashing | False | True | True | False | True| False| True
| Printer is unrecognized | True | True | True | True | False| False| False
| **Actions** 	 
| Check the power cable | x	| 
| Check the printer-computer cable | x | x | 
| Ensure printer software is installed | x | x | x |x |
| Check/replace ink | | x |x | |x ||x|
| Check for paper jam | | | | | x |x|

<br/>

Decision Table translated into MicroPython with test

```python
# Decision Table translated into MicroPython with test

# Conditions for printer issue description
conditions = ["Printer does not print", "A red light is flashing",
              "Printer is unrecognized"]  # That was 3 conditions

# Actions
Power_Cable = "Check the power cable"
Printer_Computer_Cable = "Check the printer-computer cable"
Software_Installed = "Ensure printer software is installed"
New_Ink = "Check/replace ink"
Paper_Jam = "Check for paper jam"

# Rule Set building 
rules = [((True,  False, True),  Power_Cable),
         ((True,  True,  True),  Printer_Computer_Cable),
         ((True,  False, True),  Printer_Computer_Cable),
         ((True,  True,  True),  Software_Installed),
         ((True,  False, True),  Software_Installed),
         ((False, True,  True),  Software_Installed),
         ((False, False, True),  Software_Installed),
         ((True,  True,  True),  New_Ink),
         ((True,  True,  False), New_Ink),
         ((False, True,  True),  New_Ink),
         ((False, True,  False), New_Ink),
         ((True,  True,  False), Paper_Jam),
         ((True,  False, False), Paper_Jam)
         ]

# Exec rules evaluation
def evalRule(tupl, table):
    answ = []
    for key, val in table:
        if key == tupl:
            answ.append(val)
    return answ

# test DTT
def testDTT():
    
    testcond = (False,  True, True)

    print(conditions[0], ' = ' ,testcond[0])
    print(conditions[1], ' = ' ,testcond[1])
    print(conditions[2], ' = ' ,testcond[2])

    answ = evalRule(testcond, rules) 
    print(answ)
    
    assert answ[0] == Software_Installed and answ[1]== New_Ink and len(answ)<3, "Decision Table test Fail: expected answer =" + Power_Cable
    
    print("Decision Table test: pass")

testDTT()
```
<br/>

## 4. State Transition Testing

Technique changes in input conditions which change the state of the Application Under Test (AUT). This allows the tester to test the behavior of an AUT. The tester can perform this action by entering various input conditions in a sequence. You should provide positive as well as negative input test values for evaluating the system behavior.

![State Transition Testing](/img/testtechstt.png)

Guidelines:

- State transition should be used when you are testing the application for a limited set of input values.
- and you wants to test sequence of events which happen in an AUT.

## 5. Error Guessing
Tester knows common mistakes that developers usually forget to handle:
- Divide by zero.
- Handling null values in text fields.
- Accepting the Submit button without any value.
- File upload without attachment.
- File upload with less than or more than the limit size.

So you can writes such tests to expose those common errors.

## 6. Graph-Based Testing Methods

Graph-based testing builds first a graph model for the AUT, and then tries to cover certain elements in the graph model

Rationale behind technique:
- Each and every application is a build-up of some objects. 
- All such objects are identified and the graph is prepared. 
- From this object graph, each object relationship is identified and test cases are written accordingly to discover the errors.

## 7. Comparison Testing

Different independent versions of the same software are used to compare to each other for testing in this method. For example testing comprises of comparing the contents of files, databases, against actual results.

<br/>

# Application of Testing Techniques 

In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is, and for n > 1 [wikipedia]

```python
# returns fibonacci number
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2) # recursive call 
```

![State Transition Testing](/img/fib.jpg)

Lets try to apply few testing techniques which we learned on fibonacci function example
- Boundary Values
- Error Guessing
```python
# Fibonacci

def fib(n):

# To fix Error Guessing tests uncomment this lines
#    if n is None or type(n) is str or n < 0:
#        return 0
    
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


try:
    
    #  Boundary Values technique

    assert fib(0) == 0  # test edge 0
    assert fib(1) == 1   # test edge 1
    assert fib(8) == 21  # test internal point expected 21

    #  Error Guessing technique

    assert fib(-1) == 0, "invalid value -1"  # test invalid value
    assert fib(None) == 0, "invalid value None"  # test null value
    assert fib('a') == 0, "invalid value 'a'"  # test wrong value type

    print("Fibonacci test: pass")

except AssertionError as err:
    print("Fibonacci test Fail: {0}".format(err))

# to cover all exceptions uncomment below lines
#except:
#    print("Fibonacci test Fail:An unexpected exception occurred")
```
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

### Step 6: Final implementation of standard deviation function, *std()*

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

<br/>

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

In second part of this tutorial I will cover more complex testing examples and untouched related topics

# Resources

Further reading and useful links:
- [Guru99](https://www.guru99.com/software-testing.html)
- [Software Testing Help](https://www.softwaretestinghelp.com/)
- [wikipedia Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number)
- [wikipedia Standard deviation](https://en.wikipedia.org/wiki/Standard_deviation)


# Credits


# License
Unless otherwise noted, the contents of this document are licensed under a license
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

![Creative Commons](img/cc.svg) ![by](img/by.svg) ![nc-eu](img/nc-eu.svg) ![sa](img/sa.svg)