# -*- coding: utf-8 -*-
from helpers import nfs, logger
from file_permissions import FilePermissions
from dir_permissions import DirPermissions
from file_attributes import FileAttributes


def main():
    log = logger.Log().clear_log()
    nfs_client = nfs.NfsClient()
    FilePermissions(nfs_client.files_with_permissions)
    DirPermissions(nfs_client.dirs_with_permissions)
    FileAttributes(nfs_client.rw)


main()