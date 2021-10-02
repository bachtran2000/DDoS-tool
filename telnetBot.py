
from telnetlib import Telnet
import os

class Telnet:
    def telnet(listip):
        for ip in listip:
            try:
                os.system("telnet "+ip)
            except:
                print('Could not connect. Exiting')

