
from telnetlib import Telnet

class Telnet:
    def telnet(listip):
        for ip in listip:
            try:
                tn = telnetlib.Telnet(ip)
            except:
                print('Could not connect. Exiting')

