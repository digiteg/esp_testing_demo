# -------------------------------------------------------------------------------
# Name:        MicroTestRunner
# Purpose:     Enable logging on micro controller
#
# Author:      Milan Varga
#
# Created:     13.07.2020
# Copyright:   (c) Milan Varga 2020
# Licence:     Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
# -------------------------------------------------------------------------------

import sys
import traceback
from inspect import getmembers, isfunction, getargspec, getsourcelines

from microtest.micrologger import MicroLogger
from microtest.basiclogger import LogLevels


class MicroTestRunner:

    log = None
    _test_suites_list = None

    count_passed = 0
    count_failed = 0
    count_skipped = 0
    count_error = 0

    count_expected_failures = 0
    count_unexpected_passes = 0

    def __init__(self, modglobals=None):
        self.log = MicroLogger()
        self.log.basicConfig(vlevel=LogLevels.INFO)
        self.setup(modglobals)

#    def _extract_function_name(self):
#        tb = sys.exc_info()[-1]
#        stk = traceback.extract_tb(tb, 1)
#        fname = stk[0][3]
#        return fname

    def _log_exception(self, fname, ex):
        self.log.log_error("{} raised {} ({}): {}",
                           fname,  # this is optional
                           ex.__class__,
                           ex.__doc__,
                           ex
                           )

    def _log_assertion_exception(self, fname, ex):
        self.log.log_failed("{} raised {} ({})",
                            fname,  # this is optional
                            ex.__class__,
                            ex.__doc__
                            )

    def _get_tests(self, module):

        tests = set()

        # retrive name obj of functions
        for name, fn in getmembers(module, isfunction):
            if name.startswith('test_'):  # function starts with test_
                lineno = getsourcelines(fn)[1]  # return function starting line
                tests.add((lineno, name))   # create touple list

        tests = sorted(tests)
        return tests

    def _log_start_tests_block(self, mname, mfile, count):
        self.log.log_line(
            "\n======================= Test suite Start: {} ===============================", mname)
        self.log.log_line("Loaded file: {}", mfile)
        self.log.log_line("Tests collected: {}\n", count)

    def _log_summary(self, mname):

        self.log.log_line(
            "\n======================= Summary of: {} ===============================\n", mname)
        self.log.log_line("Total Passed {}", self.count_passed)
        self.log.log_line("Total Skipped {}", self.count_skipped)
        self.log.log_line("Total Failed {}", self.count_failed)
        self.log.log_line("Total Errors {}", self.count_error)

        self.log.log_line("Expected Failures {}", self.count_expected_failures)
        self.log.log_line("Unexpected Passes {}", self.count_unexpected_passes)

    def _test_suite_counters_init(self):
        self.count_passed = 0
        self.count_failed = 0
        self.count_skipped = 0
        self.count_error = 0

        self.count_expected_failures = 0
        self.count_unexpected_passes = 0

    # Iterate within test suite as it is a collection of test cases. It is used to aggregate tests that must be run together.

    def run_test_suite(self, module, log_module_file_name=True, log_module_name=True):

        module_name = module.__name__
        module_file = module.__file__

        tests = self._get_tests(module)

        if log_module_file_name:
            self._log_start_tests_block(module_name, module_file, len(tests))

        self._test_suite_counters_init()

        for lineno, name in tests:

            # get the reference to the function from the module
            fn = getattr(module, name)
            args, varargs, varkw, defaults = getargspec(fn)

            # make the function call
            try:
                if args is None or len(args) < 1:
                    fn()
                else:
                    fn(args)

                if log_module_name:
                    self.log.log_passed("{}:{}".format(module_name, name))
                else:
                    self.log.log_passed(name)

                self.count_passed += 1

            except AssertionError as err:
                if log_module_name:
                    self._log_assertion_exception(
                        "{}:{}".format(module_name, name), err)
                else:
                    self._log_assertion_exception(name, err)
                self.count_failed += 1

            except Exception as e:
                self._log_exception(name, e)
                self.count_error += 1

        self._log_summary(module_name)

    # return Test suites = modules starting with test_
    def _get_test_modules(self, modlist):
        test_sets = set()
        position = 0
        # retrive name obj of functions
        for module_name, obj in modlist.items():
            if module_name.startswith('test_'):  # function starts with test_
                position += 1  # add number
                # create touple list
                test_sets.add((position, module_name, obj))

        return sorted(test_sets)

    # test runner is a component that organizes the execution of tests and provides the result to the user.
    def exec(self, log_module_file_name=True, log_module_name=False):

        if self._test_suites_list is None:
            self.log.log_line("None Test Suites and Tests founded")
            return

        for pos, module_name, obj in self._test_suites_list:
            self.run_test_suite(obj, log_module_file_name, log_module_name)

    def setup(self, modglobals):
        if modglobals is not None:
            self._test_suites_list = self._get_test_modules(modglobals)
        else:
            self._test_suites_list = None

    def clear(self):
        if self.log is not None:
            self.log.clear()

    def __del__(self):
        self.clear()
