# -*- coding: utf-8 -*-
from nfs_client import client
from file_permissions import FilePermissions
from dir_permissions import DirPermissions



def main():
    nfs_client = client.NfsClient()
    FilePermissions(nfs_client.files_with_permissions)
    DirPermissions(nfs_client.dirs_with_permissions)
    pass


main()