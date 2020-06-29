""""
Unit Tests Are Just Functions
Unit tests are typically made of three pieces, some set-up, a number of assertions, and some tear-down. 
Set-up can be as simple as initializing the input values or as complex as creating and initializing concrete instances of a class. 
Ultimately, the test occurs when an assertion is made, comparing the observed and expected values. For example, let us test that our mean function successfully calculates the known value for a simple list.
"""

try:
    assert "Hello" == "Hello"
    assert 3 == 2, "Failed"
    print("Test : pass")

except AssertionError as err:
    print("Test Assertion error: {0}".format(err))
except:
    print("An unexpected exception occurred")

# Array ------------------------------


test_list1 = [1, 2, 4, 3, 5]
test_list2 = [1, 2, 4, 3, 5]

assert test_list1 == test_list2
print("Array Test : pass")

# ------------------------------

thistuple1 = ("apple", "banana", "cherry")
thistuple2 = ("apple", "banana", "cherry")

assert thistuple1 == thistuple2
print("Tuple Test : pass")

# ------------------------------


thisset1 = {"apple", "banana", "cherry"}
thisset2 = {"apple", "banana", "cherry"}

assert thisset1 == thisset2
print("Set test: pass")


# ------------------------------

thisdict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

assert thisdict1 == thisdict2
print("Dictionary test: pass")

# --------------------------------------------------------------------------------------------

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

# --------------------------------------------------------------------------------------------
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


# --------------------------------------------------------------------------------------------
# Decision Table Testing



conditions = ["Printer does not print", "A red light is flashing",
              "Printer is unrecognised"]  # That was 3 conditions

Power_Cable = "Check the power cable"
Printer_Computer_Cable = "Check the printer-computer cable"
Software_Installed = "Ensure printer software is installed"
New_Ink = "Check/replace ink"
Paper_Jam = "Check for paper jam"


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

def evalRule(tupl, table):
    answ = []
    for key, val in table:
        if key == tupl:
            answ.append(val)
    return answ

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


# --------------------------------------------------------------------------------------------
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

