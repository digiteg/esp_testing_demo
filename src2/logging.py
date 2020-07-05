import sys


CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0


class _BasicLogger:

    _level = NOTSET
    _write_level_name = False
    _write_name = False

    _level_dict = {
        CRITICAL: "CRITICAL",
        ERROR: "ERROR",
        WARNING: "WARNING",
        INFO: "INFO",
        DEBUG: "DEBUG",
    }

    def __init__(self, name, vlevel=NOTSET, wlevel_name=True, vwrite_name=True):
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
        self.log(DEBUG, msg, *args)

    def log_info(self, msg, *args):
        self.log(INFO, msg, *args)

    def log_warning(self, msg, *args):
        self.log(WARNING, msg, *args)

    def log_error(self, msg, *args):
        self.log(ERROR, msg, *args)

    def log_critical(self, msg, *args):
        self.log(CRITICAL, msg, *args)


class TextLogger(_BasicLogger):
    def write(self, message):
        print(message)

    def write_level_name(self, blev, isname=False):
        if isname:
            print("{}:{}:".format(blev, self.name), end="")
        else:
            print("{}:".format(blev), end="")


class FileLogger(_BasicLogger):

    _file = None

    def __init__(self, name, logfile, vlevel=NOTSET, wlevel_name=True, vwrite_name=True):
        super().__init__(name, vlevel, wlevel_name, vwrite_name)
        f = open(logfile, 'w')
        self._file = f


    def write_end_line(self):
        if(self._file != None and not self._file.closed):
            self._file.write("\n")

    def write_level_name(self, blev, isname=False):
        if isname:
            self._file.write("{}:{}:".format(blev, self.name))
        else:
            self._file.write("{}:".format(blev))

    def write(self, message):
        if(self._file != None and not self._file.closed):
            self._file.write(message)


    def flush(self):
        if(self._file != None and not self._file.closed):
            self._file.flush()

    def close(self):
        self.flush()
        if(self._file != None and not self._file.closed):
            self._file.close()

    @property
    def logfile(self):
        return self._file

    @logfile.setter
    def logfile(self, infile):
        self._file = infile

    def __del__(self):
        self.close()


class LogRunner:

    _loggers = {}

    def createTextLogger(self, name, vlevel=NOTSET, wlevel_name=True, vwrite_name=True):
        tmplog = TextLogger(name, vlevel, wlevel_name, vwrite_name)
        self._loggers[name] = tmplog
        return tmplog

    def createFileLogger(self, name, logfile, vlevel=NOTSET, wlevel_name=True, vwrite_name=True):
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

    def basicConfig(self, name="Logger", filename="logfile.log", vlevel=INFO, wlevel_name=True, vwrite_name=False):

        self.createTextLogger(name+"Text", vlevel, wlevel_name, vwrite_name)
        if filename is not None:
            self.createFileLogger(name+"File", filename, vlevel,
                                  wlevel_name, vwrite_name)
