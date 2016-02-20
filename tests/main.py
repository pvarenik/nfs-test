# -*- coding: utf-8 -*-
from nfs_client import client


def main():
    nfs_client = client.NfsClient()
    nfs_client.connect()


main()