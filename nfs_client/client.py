# -*- coding: utf-8 -*-
import ConfigParser
import os


class NfsClient():
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("../config.cfg")
        self.path = Config.get('PARAMETERS', 'MOUNT_POINT')
        self.dirs = []
        self.files = []
        self.files_with_permissions = {}
        self.writable = []
        self.readable = []
        self.executable = []
        self.get_all()
        assert os.path.exists(self.path), "path doesn't exist"

    def get_all(self):
        for dirname, dirnames, filenames in os.walk(self.path):
            # get folders
            for subdirname in dirnames:
                self.dirs.append(os.path.join(dirname, subdirname))
            # get files
            for filename in filenames:
                file = os.path.join(dirname, filename)
                self.files.append(file)
                if (os.access(file, os.W_OK)):
                    self.writable.append(file)
                elif (os.access(file, os.R_OK)):
                    self.readable.append(file)
                elif (os.access(file, os.X_OK)):
                    self.executable.append(file)

            self.files_with_permissions["w"] = self.writable
            self.files_with_permissions["r"] = self.readable
            self.files_with_permissions["x"] = self.executable
            # assert len(self.files) > 0 and len(self.dirs) > 0, "path is empty"
