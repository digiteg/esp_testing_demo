# Test fixture: test fixture is the fixed state of the objects used as the source when performing tests.
# The purpose of using fixture is if you have a complex test case, then preparing the desired state can easily take a lot of resources
# (for example, you consider a function with certain accuracy and each next sign of accuracy in the calculations takes a day).
# Using fixture (on slang - fixtures), we skip the preliminary preparation of the state and immediately begin testing.
# Test fixture can appear, for example, in the form (database state, set of environment variables, set of files with the necessary content).

# importing libraries
import time
import math

from datetime import datetime, timedelta


class SkipTest(Exception):
    pass


def skip(msg):
    def _decor(fun):
        # We just replace original fun with _inner
        def _inner(self):
            raise SkipTest(msg)
        return _inner
    return _decor


def skipIf(cond, msg):
    if not cond:
        return lambda x: x
    return skip(msg)


def skipUnless(cond, msg):
    if cond:
        return lambda x: x
    return skip(msg)


# --------------------------------------- Decorator Fixture


def noparam(func):

    def inner1():
        begin = time.time()

        # calling the actual function now
        # inside the wrapper function.
        func()

        #print("This is after function execution")
        # storing time after function execution
        end = time.time()
        print("Total time taken in {} : {} ".format( func.__name__, end - begin))

    return inner1


# --------------------------



def multiparam(decorator_args):

    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(func):

        def wrapper(*args, **kwargs):

            begin = time.time()
            for values in decorator_args:
                func(*values)

            # storing time after all params execution
            end = time.time()

            print("Total time taken in {} : {} ".format( func.__name__, end - begin))

            # storing time before original call function execution
            # func(*args, **kwargs)  - stop call

        return wrapper
    return inner1









"""

import utime

t = utime.ticks_us()

delta = utime.ticks_diff(utime.ticks_us(), t) 
print('Function {} Time = {:6.3f}ms'.format(name, delta/1000))

"""


# decorator to calculate duration
# taken by any function.
def calculate_time(func):

    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)


# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
def memoize_factorial(f):
    memory = {}

    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1)


print(facto(5))


#------------------------------------


def decorator_func(x, y):

    def Inner(func):

        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x+y))

            func(*args, **kwargs)

        return wrapper
    return Inner


# --------------------

testdata = [(datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
            (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
            ]


@multiparam(testdata)
def test_timedistance_v0(a, b, expected):

    diff = a - b
    print("Test: {} - {} = {}".format(a, b, diff))
    assert diff == expected


test_timedistance_v0()


# ---------------------
def f(a, b, y, x):
    print(a, b, x, y)


d = {'a': 'append', 'b': 'block', 'x': 'extract', 'y': 'yes'}
f(**d)
