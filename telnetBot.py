
from telnetlib import Telnet
import os
from multiprocessing import Process

class Telnet:
    def telnet(ip):
        try:
            os.system("telnet "+ip)

        except:                
            print('Could not connect. Exiting')

