# -------------------------------------------------------------------------------
# Name:        TextLogger, FileLogger
# Purpose:     Enable print or write log message into file on micro controller
#
# Author:      Milan Varga
#
# Created:     13.07.2020
# Copyright:   (c) Milan Varga 2020
# Licence:     Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
# -------------------------------------------------------------------------------

from microtest.basiclogger import _BasicLogger, LogLevels

# Text Logger prints message
class TextLogger(_BasicLogger):
    def write(self, message):
        print(message)

    def write_level_name(self, blev, isname=False):
        if isname:
            print("{}:{}: ".format(blev, self.name), end="")
        else:
            print("{}: ".format(blev), end="")

# File Logger stores message into file
class FileLogger(_BasicLogger):

    _file = None

    def __init__(self, name, logfile, vlevel=LogLevels.NOTSET, wlevel_name=True, vwrite_name=True):
        super().__init__(name, vlevel, wlevel_name, vwrite_name)
        f = open(logfile, 'w')
        self._file = f

    def write_end_line(self):
        if(self._file != None and not self._file.closed):
            self._file.write("\n")

    def write_level_name(self, blev, isname=False):
        if isname:
            self._file.write("{}:{}: ".format(blev, self.name))
        else:
            self._file.write("{}: ".format(blev))

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

