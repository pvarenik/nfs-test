import os
import datetime
from random import randint


class FileAttributes():
    def __init__(self, writable_files):
        print "\n[ Files attributes tests ]"
        self.flag = True
        self.change_modification_time_test(writable_files)
        self.change_access_time_test(writable_files)

    def change_modification_time_test(self, writable_files):
        self.flag = True
        for file in writable_files:
            year = randint(1971, 2016)
            month = randint(0, 12)
            day = randint(0, 28)
            adate = os.stat(file).st_atime
            mdate = os.stat(file).st_mtime
            d = (datetime.datetime(year, month, day) - datetime.datetime(1970, 1, 1)).total_seconds()
            os.utime(file, (adate, d))
            new_mdate = os.stat(file).st_mtime
            if mdate == new_mdate and new_mdate != d:
                self.flag = False
        print "change_modification_time_test: " + str(self.flag)

    def change_access_time_test(self, writable_files):
        self.flag = True
        for file in writable_files:
            year = randint(1971, 2016)
            month = randint(0, 12)
            day = randint(0, 28)
            adate = os.stat(file).st_atime
            mdate = os.stat(file).st_mtime
            d = (datetime.datetime(year, month, day) - datetime.datetime(1970, 1, 1)).total_seconds()
            os.utime(file, (d, mdate))
            new_adate = os.stat(file).st_atime
            if adate == new_adate and new_adate != d:
                self.flag = False
        print "change_access_time_test: " + str(self.flag)
