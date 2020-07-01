# **ESP8266 Simple Testing with examples in Micropython**

I was digging on internet for some examples about testing on ESP8266 in Micropython just for myself education purpose and I didn't find too much useful examples for me. So I decided to fill this gap and I hope this can be  also useful for others who are willing to deal with the topic or teach their students about basics and how to automate testing. Why ESP8266 ? Because it is cost-effective and highly integrated Wi-Fi MCU for IoT / smart things... applications


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
# Things used in this project

### **Hardware components**

 Things used in this project
 ![NodeMCU ESP8266](/img/ESP8266.jpg)

### **Hardware components**

||Name|Qt||
| :---|:------------------------:|:---| ----:|
| Img | Raspberry Pi 3 Model B	 | ×1 | link |
| Img | Raspberry Pi 3 Model B	 | ×1 | link |
| Img | Raspberry Pi 3 Model B	 | ×1 | link |
| Img | Raspberry Pi 3 Model B	 | ×1 | link |
| Img | Raspberry Pi 3 Model B	 | ×1 | link |

### **Software apps and online services**
||Name|Qt||
| :---|:------------------------:|:---| ----:|
| Img | Raspberry Pi 3 Model B	 | ×1 | link |

### **Hand tools and fabrication machines**
||Name|Qt||
| :---|:------------------------:|:---| ----:|
| Img | Raspberry Pi 3 Model B	 | ×1 | link |

<br/>

# Long story short

Why Did We Build This?
Idea 💡
Hardware Build


![Types of Testing](/img/typestesting.png)



## **Getting Started with first level - Unit Tests are just functions**


- **Unit tests** are typically made of three pieces, some **setup**, a number of **assertions**, and some **tear-down**. 

- **Setup** can be as simple as initializing the input values or as complex as creating and initializing concrete instances of a class. 

- **Execution**, the test occurs when an assertion is made, comparing the observed and expected values. For example, let us test  that our mean function successfully calculates the known value for a simple list.

Try to copy and paste following code examples into REPL

### Step 1: MicroPython hello _**assert**_ Keyword

The assert keyword is usually used when we debugging or and lets you test if a condition in your code returns *True*, if not, the program will raise an *AssertionError*.
You can also add a message to be written if the code returns False, check the examples below.

```python
x = "hello Micropython"
    
#if condition returns True, then nothing happens:
assert x == "hello Micropython"
    
#if condition returns False, AssertionError is raised:
assert x == "bye"
```
### Step 2:  Add message

Write a message if the condition is False

```python
x = "hello Micropython"

#if condition returns False, AssertionError is raised:

assert x == "bye", "x should be 'hello Micropython'"
```
### Step 3: Handle *AssertionError* exceptions with  _**try**_ / _**except**_ / _**finally**_ block

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

### Step 4:

```python
# Array Test:

test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]

assert test_list1 == test_list2
print("Array test : pass")
```
### Step 5:

```python
# Tuple Test:

test_tuple1 = ("apple", "banana", "cherry")
test_tuple2 = ("apple", "banana", "cherry")

assert test_tuple1 == test_tuple2
print("Tuple test : pass")
```
### Step 6:

```python
# Set test

test_set1 = {"apple", "banana", "cherry"}
test_set2 = {"apple", "banana", "cherry"}

assert test_set1 == test_set2
print("Set test: pass")
```
### Step 7:

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



# Testing Techniques 

## 1. Equivalence Partitioning
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
## 3. Decision Table Testing

Following example covers 3 clearly distinguished printer issues with how to fix them actions translated into **Decision table**

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
## 4. State Transition Testing
![State Transition Testing](/img/testtechstt.png)

## 5. Error Guessing
Tester knows common mistakes that developers usually forget to handle:
- Divide by zero.
- Handling null values in text fields.
- Accepting the Submit button without any value.
- File upload without attachment.
- File upload with less than or more than the limit size.

## 6. Graph-Based Testing Methods
- Each and every application is a build-up of some objects. 
- All such objects are identified and the graph is prepared. 
- From this object graph, each object relationship is identified and test cases are written accordingly to discover the errors.

## 7. Comparison Testing
- Different independent versions of the same software are used to compare to each other for testing in this method.



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

Lets try few testing techniques applied on fibonacci function example
- Boundary Values
- Error Guessing
```python
# Fibonacci

def fib(n):
    
#    if n is None or type(n) is str or n < 0:
#        return 0
    
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


try:
    assert fib(0) == 0  # test edge 0
    assert fib(1) == 1   # test edge 1
    assert fib(8) == 21  # test internal point expected 21

    assert fib(-1) == 0, "invalid value -1"  # test invalid value
    assert fib(None) == 0, "invalid value None"  # test null value
    assert fib('a') == 0, "invalid value 'a'"  # test wrong value type


    print("Fibonacci test: pass")

except AssertionError as err:
    print("Fibonacci test Fail: {0}".format(err))
#except:
#    print("Fibonacci test Fail:An unexpected exception occurred")
```

# Test Driven Development

### Step 1:
### Step 2:
### Step 3:

```python
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
```

### Step 4:

```python
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
```


# Integration Test - Example

```python
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
```

# Next steps

# Resources


# Credits


# License

Pokiaľ nie je uvedené inak, obsah tohto dokumentu je licencovaný licenciou [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

![Creative Commons](img/cc.svg) ![by](img/by.svg) ![nc-eu](img/nc-eu.svg) ![sa](img/sa.svg)