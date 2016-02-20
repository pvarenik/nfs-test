# -*- coding: utf-8 -*-
from subprocess import *
import ConfigParser
import platform
import os


class NfsClient():
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("../config.cfg")
        self.host = Config.get('Host parameters', 'HOST')
        self.path = Config.get('Host parameters', 'PATH')
        self.share_path = Config.get('Local parameters', 'SHARE_PATH')

    def connect(self):
        if (not os.path.exists(self.share_path)):
            check_call(['mkdir', self.share_path])
        if (platform.system() == "Windows"):
            check_call(["c:\Windows\SysWOW64\cmd.exe", "/c", "mount.exe", self.host + ":" + self.path, self.share_path],
                       shell=True)

            check_call(["mount", self.host + ":" + self.path, self.share_path], shell=True)
        else:
            check_call(["sudo", "mount", self.host + ":" + self.path, self.share_path])
