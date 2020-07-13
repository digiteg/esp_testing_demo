# -------------------------------------------------------------------------------
# Name:        MicroLog
# Purpose:     Enable logging on micro controller
#
# Author:      Milan Varga
#
# Created:     13.07.2020
# Copyright:   (c) Milan Varga 2020
# Licence:     Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
# -------------------------------------------------------------------------------


from microtest.basiclogger import LogLevels
from microtest.mclogger import TextLogger, FileLogger


class MicroLogger:

    _loggers = {}

    def createTextLogger(self, name, vlevel=LogLevels.NOTSET, wlevel_name=True, vwrite_name=True):
        tmplog = TextLogger(name, vlevel, wlevel_name, vwrite_name)
        self._loggers[name] = tmplog
        return tmplog

    def createFileLogger(self, name, logfile, vlevel=LogLevels.NOTSET, wlevel_name=True, vwrite_name=True):
        tmplog = FileLogger(name, logfile, vlevel, wlevel_name, vwrite_name)
        self._loggers[name] = tmplog
        return tmplog

    def getLogger(self, name):
        if name in self._loggers:
            return self._loggers[name]
        return None

    def log_line(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_line(msg, *args)

    # log level
    def log_debug(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_debug(msg, *args)

    def log_info(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_info(msg, *args)

    def log_warning(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_warning(msg, *args)

    def log_error(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_error(msg, *args)

    def log_critical(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_critical(msg, *args)


    # log test

    def log_passed(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_passed(msg, *args)


    def log_failed(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_failed(msg, *args)


    def log_skipped(self, msg, *args):
        for logger in self._loggers.values():
            logger.log_skipped(msg, *args)



    # stream

    def flush(self):
        for logger in self._loggers.values():
            logger.flush()

    def close(self):
        self.flush()
        for logger in self._loggers.values():
            logger.close()

    def clear(self):
        self.close()
        self._loggers.clear()

    def __del__(self):
        self.clear()

    def basicConfig(self, name="Logger", filename="logfile.log", vlevel=LogLevels.INFO, wlevel_name=True, vwrite_name=False):

        self.createTextLogger(name+"Text", vlevel, wlevel_name, vwrite_name)
        if filename is not None:
            self.createFileLogger(name+"File", filename, vlevel,
                                  wlevel_name, vwrite_name)
