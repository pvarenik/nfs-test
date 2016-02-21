# -*- coding: utf-8 -*-
import ConfigParser
import os
from helpers import logger


class NfsClient():
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("../config.cfg")
        self.log = logger.Log().log_line
        self.path = Config.get('PARAMETERS', 'MOUNT_POINT')
        self.dirs = []
        self.rdir = []
        self.wdir = []
        self.dirs_with_permissions = {}
        self.files = []
        self.files_with_permissions = {}
        self.rw = []
        self.rx = []
        self.r = []
        self.get_all()
        if (os.path.exists(self.path)):
            self.log("path %s doesn't exist" % self.path)
            assert os.path.exists(self.path), "path doesn't exist"



    def get_all(self):
        self.log("Getting all files and subdirs in %s directory:" % self.path)
        for dirname, dirnames, filenames in os.walk(self.path):
            spaces = 0
            # get folders
            for subdirname in dirnames:
                dir_name = os.path.join(dirname, subdirname)
                self.log("[%s]" % dir_name)
                spaces += 1
                self.dirs.append(dir_name)
                perm = int(oct(os.stat(dir_name).st_mode)[-3:])
                if perm > 333:
                    self.rdir.append(dir_name)
                else:
                    self.wdir.append(dir_name)
            # get files
            for filename in filenames:
                file = os.path.join(dirname, filename)
                self.log("%s" % file)
                self.files.append(file)
                perm = int(oct(os.stat(file).st_mode)[-3:])
                if perm > 555:
                    self.rw.append(file)
                elif perm > 444:
                    self.rx.append(file)
                elif perm > 333:
                    self.r.append(file)
        self.dirs_with_permissions["read"] = self.rdir
        self.dirs_with_permissions["cant_read"] = self.wdir
        self.files_with_permissions["rw"] = self.rw
        self.files_with_permissions["rx"] = self.rx
        self.files_with_permissions["r"] = self.r
        self.log("Directory %s scanned" % self.path)
