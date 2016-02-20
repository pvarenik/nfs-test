import os


class DirPermissions():
    def __init__(self, dirs):
        print "\n[ Dirs permissions tests ]"
        self.flag = True
        self.writable_test(dirs)
        self.readable_test(dirs)

    def writable_test(self, dirs):
        self.flag = True
        for wdir in dirs["cant_read"]:
            try:
                os.listdir(wdir)
                self.flag = False
            except OSError:
                pass
        print "writable_test: " + str(self.flag)

    def readable_test(self, dirs):
        self.flag = True
        for rdir in dirs["read"]:
            try:
                os.listdir(rdir)
            except OSError:
                self.flag = False
        print "readable_test: " + str(self.flag)
