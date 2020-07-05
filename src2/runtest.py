
import sys
import traceback
from inspect import getmembers, isfunction, getargspec

import logging

import wallet

log = logging.LogRunner()
log.basicConfig(vlevel=logging.INFO)

def extract_function_name():
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        fname = stk[0][3]
        return fname

def log_exception(ex):
        log.log_error("Function {} raised {} ({}): {}",
                 extract_function_name(),  # this is optional
                 ex.__class__,
                 ex.__doc__,
                 ex
                 )


def get_tests(module):

    tests = set()

    for name, data in getmembers(module, isfunction):
        if name.startswith('test_'):
            tests.add(name)  # [5:]
    return tests


tests = get_tests(wallet)
print(tests)

for name in tests:
    # get the reference to the function from the module
    fn = getattr(wallet, name)
    args, varargs, varkw, defaults = getargspec(fn)
    # make the function call

    try:
        if args is None or len(args) < 1:
            fn()
        else:
            fn(args)
        log.log_line("{} :pass".format(name))
    except Exception as e:
        log_exception(e)


# for name, data in getmembers(wallet, isfunction):
#    print ("{}: {}".format( name, repr(data)))
#    name()


#fcn_list = [o[0] for o in getmembers(wallet, isfunction)]
#print(fcn_list)

"""
test_uppercase()
test_reversed()
test_some_primes()

say_whee(data)
"""
