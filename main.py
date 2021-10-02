from scan_device import Scanbot
from telnetBot import Telnet

listip = Scanbot.scan()

Scanbot.display_result(listip)

Telnet.telnet(listip)


