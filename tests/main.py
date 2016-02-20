# -*- coding: utf-8 -*-
from nfs_client import client
from permissions import Permissions


def main():
    nfs_client = client.NfsClient()
    Permissions(nfs_client.files_with_permissions)
    pass


main()