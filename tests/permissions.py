import random
import string


class Permissions():
    def __init__(self, files):
        print "writable_test: " + str(self.writable_test(files))
        print "readable_test: " + str(self.readable_test(files))
        print "executable_test: " + str(self.executable_test(files))

    def writable_test(self, files):
        flag = True
        random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100))
        for w in files["rw"]:
            file = open(w, "w")
            file.write(random_str)
            file.close()
            file = open(w, "r")
            self.flag = random_str == file.read()
            file.close()
        return flag

    def readable_test(self, files):
        flag = True
        for r in files["r"]:
            file = open(r, "r")
            file.close()
        return flag

    def executable_test(self, files):
        flag = True
        for r in files["rx"]:
            file = open(r, "r")
            file.close()
        return flag
