""" SFTP connection example

    Using the paramiko library to perform a SFTP file transfer
"""
import sys

import paramiko

port = 22

transport = paramiko.Transport(("host", port))
transport.connect(username="user", password="secret")

sftp = paramiko.SFTPClient.from_transport(transport)

localpath = sys.argv[1]

path = './target/directory/' + localpath
sftp.put(localpath, path)

sftp.close()
transport.close()
print('uploaded')

