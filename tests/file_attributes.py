import os
from datetime import datetime
from random import randint
from helpers import logger


class FileAttributes():
    def __init__(self, writable_files):
        self.log = logger.Log().log_line
        self.log("[ Files attributes tests ]")
        print "\n[ Files attributes tests ]"
        self.flag = True
        self.change_modification_time_test(writable_files)
        self.change_access_time_test(writable_files)

    def change_modification_time_test(self, writable_files):
        self.log("START: change_modification_time_test")
        self.flag = True
        for file in writable_files:
            year = randint(1971, 2016)
            month = randint(1, 12)
            day = randint(1, 28)
            adate = os.stat(file).st_atime
            mdate = os.stat(file).st_mtime
            d = (datetime(year, month, day) - datetime(1970, 1, 1)).total_seconds()
            self.log("Change file {0} modification date from {1} to {2}".format(file, datetime.fromtimestamp(mdate),
                                                                                datetime.fromtimestamp(d)))
            os.utime(file, (adate, d))
            new_mdate = os.stat(file).st_mtime
            if mdate == new_mdate and new_mdate != d:
                self.flag = False
                self.log("Not passed")
        self.log("RESULT: change_modification_time_test: " + str(self.flag))
        print "change_modification_time_test: " + str(self.flag)

    def change_access_time_test(self, writable_files):
        self.log("START: change_access_time_test")
        self.flag = True
        for file in writable_files:
            year = randint(1971, 2016)
            month = randint(1, 12)
            day = randint(1, 28)
            adate = os.stat(file).st_atime
            mdate = os.stat(file).st_mtime
            d = (datetime(year, month, day) - datetime(1970, 1, 1)).total_seconds()
            self.log("Change file {0} access date from {1} to {2}".format(file, datetime.fromtimestamp(adate),
                                                                          datetime.fromtimestamp(d)))
            os.utime(file, (d, mdate))
            new_adate = os.stat(file).st_atime
            if adate == new_adate and new_adate != d:
                self.flag = False
                self.log("Not passed")
        self.log("RESULT: change_access_time_test: " + str(self.flag))
        print "change_access_time_test: " + str(self.flag)
