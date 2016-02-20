import random
import string


class Permissions():
    def __init__(self, files):
        self.flag = True
        self.writable_test(files)

    def writable_test(self, files):

        random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100))
        for w in files["w"]:
            file = open(w, "w")
            file.write(random_str)
            file.close()
            file = open(w, "r")
            self.flag = random_str == file.read()
            file.close()
        for r in files["r"]:
            file = open(w, "w")
            file.write(random_str)
            file.close()
            file = open(w, "r")
            self.flag = random_str == file.read()
            file.close()
            pass
