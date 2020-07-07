import sys
import traceback
from inspect import getmembers, isfunction, getargspec, getsourcelines

import logging


class Microtest:

    log = None

    count_passed = 0
    count_failed = 0
    count_skipped = 0
    count_error = 0

    count_expected_failures = 0
    count_unexpected_passes = 0

    def __init__(self):
        self.log = logging.LogRunner()
        self.log.basicConfig(vlevel=logging.INFO)

    def _extract_function_name(self):
        tb = sys.exc_info()[-1]
        stk = traceback.extract_tb(tb, 1)
        fname = stk[0][3]
        return fname

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

    def _log_start_test_block(self, mname, mfile):
        self.log.log_line(
            "\n======================= Testing block: {} ===============================", mname)
        self.log.log_line("Starting tests from file {}\n", mfile)

    def _log_summary(self, mname):

        self.log.log_line(
            "\n======================= Summary {} ===============================\n", mname)
        self.log.log_line("Total Passed {}", self.count_passed)
        self.log.log_line("Total Skipped {}", self.count_skipped)
        self.log.log_line("Total Failed {}", self.count_failed)
        self.log.log_line("Total Errors {}", self.count_error)

        self.log.log_line("Expected Failures {}", self.count_expected_failures)
        self.log.log_line("Unexpected Passes {}", self.count_unexpected_passes)

    def run_test(self, module, log_module_file=True, log_module=True):

        module_name = module.__name__
        module_file = module.__file__

        if log_module_file:
            self._log_start_test_block(module_name, module_file)

        tests = self._get_tests(module)

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

                if log_module:
                    self.log.log_passed("{}:{}".format(module_name, name))
                else:
                    self.log.log_passed(name)

                self.count_passed += 1

            except AssertionError as err:
                if log_module:
                    self._log_assertion_exception(
                        "{}:{}".format(module_name, name), err)
                else:
                    self._log_assertion_exception(name, err)
                self.count_failed += 1

            except Exception as e:
                self._log_exception(name, e)
                self.count_error += 1

        self._log_summary(module_name)

        def setup(self):
            pass

        def clear(self):
            if log is not None:
                self.log.clear()

        def __del__(self):
            self.clear()