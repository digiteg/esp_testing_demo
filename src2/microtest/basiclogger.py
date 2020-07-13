# -------------------------------------------------------------------------------
# Name:        _BasicLogger, LogLevels
# Purpose:     Basic Logger functionality on micro controller
#
# Author:      Milan Varga
#
# Created:     13.07.2020
# Copyright:   (c) Milan Varga 2020
# Licence:     Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
# -------------------------------------------------------------------------------

import sys

class LogLevels:
    CRITICAL = 80
    ERROR = 70

    FAILED = 60
    PASSED = 50
    SKIPPED = 40

    WARNING = 30
    INFO = 20
    DEBUG = 10
    NOTSET = 0


class _BasicLogger:

    _level = LogLevels.NOTSET
    _write_level_name = False
    _write_name = False
    
    _level_dict = {
        LogLevels.CRITICAL: "CRITICAL",
        LogLevels.ERROR: "ERROR",
        LogLevels.WARNING: "WARNING",
        LogLevels.INFO: "INFO",
        LogLevels.DEBUG: "DEBUG",
        LogLevels.FAILED: "FAILED",
        LogLevels.PASSED: "PASSED",
        LogLevels.SKIPPED: "SKIPPED"
    }

    def __init__(self, name, vlevel=LogLevels.NOTSET, wlevel_name=True, vwrite_name=True):
        self.name = name
        self.level = vlevel
        self._print_level_name = wlevel_name
        self._write_name = vwrite_name


    def _level_str(self, level):
        actuallevel = self._level_dict.get(level)
        if actuallevel is not None:
            return actuallevel
        return "LVL " + str(_level)

    # -------------- Level property
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, vlevel):
        self._level = vlevel

    @property
    def is_level_name(self):
        return self._write_level_name

    @is_level_name.setter
    def is_level_name(self, vlevel):
        self._write_level_name = vlevel

    @property
    def is_name(self):
        return self._write_name

    @is_name.setter
    def is_name(self, vname):
        self._write_name = vname

    # ------------- Stream

    def write(self, message):
        pass

    def flush(self):
        pass

    def close(self):
        pass

    # ------------------------

    # check if enabled for level
    def isEnabledFor(self, vlevel):
        return vlevel >= self._level

    def write_level_name(self, blev, isname=False):
        pass

    def write_end_line(self):
        pass

    # log message
    def log(self, vlevel, msg, *args):
        if vlevel >= self._level:
            if self._print_level_name:
                self.write_level_name(
                    self._level_str(vlevel), self._write_name)
            self.log_line(msg, *args)

    # log text line
    def log_line(self, msg, *args):
        if not args:
            self.write(msg)
        elif msg is not None:
            self.write(msg.format(*args))
        self.write_end_line()

    # log level
    def log_debug(self, msg, *args):
        self.log(LogLevels.DEBUG, msg, *args)

    def log_info(self, msg, *args):
        self.log(LogLevels.INFO, msg, *args)

    def log_warning(self, msg, *args):
        self.log(LogLevels.WARNING, msg, *args)

    def log_error(self, msg, *args):
        self.log(LogLevels.ERROR, msg, *args)

    def log_critical(self, msg, *args):
        self.log(LogLevels.CRITICAL, msg, *args)

    # log Tests 
    def log_passed(self, msg, *args):
        self.log(LogLevels.PASSED, msg, *args)

    def log_failed(self, msg, *args):
        self.log(LogLevels.FAILED, msg, *args)

    def log_skipped(self, msg, *args):
        self.log(LogLevels.SKIPPED, msg, *args)