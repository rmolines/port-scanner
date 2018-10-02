#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p',
    required=True,
    help='port range',
    type=str )
parser.add_argument('-prot',
    help='protocol type',
    type=str,
    default='TCP' )
args = parser.parse_args()

ind = args.p.find("-")
    
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)


try:
    for port in range(int(args.p[:ind]), int(args.p[ind+1:])):  
        if(args.prot == "TCP"):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif (args.prot == "UDP"):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            raise ValueError ('wrong protocol')

        result = sock.connect_ex((remoteServerIP, port))

        if result == 0:
            print ("Port {}: 	 Open".format(port))
            sock.send('Hello, is it me you\'re looking for? \r\n'.encode())
            ret = sock.recv(1024).decode()
            print ('[+]' + str(ret))
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()