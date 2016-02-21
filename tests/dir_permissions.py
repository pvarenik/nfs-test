import os
from helpers import logger


class DirPermissions():
    def __init__(self, dirs):
        self.log = logger.Log().log_line
        self.log("[ Dirs permissions tests ]")
        print "\n[ Dirs permissions tests ]"
        self.flag = True
        self.writable_test(dirs)
        self.readable_test(dirs)

    def writable_test(self, dirs):
        self.log("START: writable_test")
        self.flag = True
        for wdir in dirs["cant_read"]:
            self.log("Try to read dir: %s. Expected: False" % wdir)
            try:
                os.listdir(wdir)
                self.flag = False
                self.log("Not passed")
            except OSError:
                pass
        self.log("RESULT: change_modification_time_test: " + str(self.flag))
        print "writable_test: " + str(self.flag)

    def readable_test(self, dirs):
        self.log("START: readable_test")
        self.flag = True
        for rdir in dirs["read"]:
            self.log("Try to read dir: %s. Expected: True" % rdir)
            try:
                os.listdir(rdir)
            except OSError:
                self.flag = False
                self.log("Not passed")
        self.log("RESULT: change_modification_time_test: " + str(self.flag))
        print "readable_test: " + str(self.flag)
