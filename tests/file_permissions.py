import random
import string


class FilePermissions():
    def __init__(self, files):
        print "\n[ Files permissions tests ]"
        self.flag = True
        self.writable_test(files)
        self.readable_test(files)
        self.executable_test(files)

    def writable_test(self, files):
        self.flag = True
        for rw in files["rw"]:
            self.try_to_write(rw, True)
            self.try_to_read(rw, True)
        print "writable_test: " + str(self.flag)

    def readable_test(self, files):
        self.flag = True
        for r in files["r"]:
            self.try_to_read(r, True)
            self.try_to_write(r, False)
        print "readable_test: " + str(self.flag)

    def executable_test(self, files):
        self.flag = True
        for r in files["r"]:
            self.try_to_read(r, True)
            self.try_to_write(r, False)
        print "executable_test: " + str(self.flag)

    def try_to_write(self, path, expected):
        result = expected
        random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100))
        try:
            file = open(path, "w")
            file.write(random_str)
            file.close()
            file = open(path, "r")
            self.flag = random_str == file.read()
            file.close()
        except IOError:
            result = not expected
        self.flag = result

    def try_to_read(self, path, expected):
        result = expected
        try:
            file = open(path, "r")
            file.close()
        except IOError:
            result = not expected
        self.flag = result
