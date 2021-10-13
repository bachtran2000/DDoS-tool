import scapy.all as scapy
import argparse
import netifaces as ni

class Scanbot:       

    def scan():
        try:
            ni.ifaddresses('en0')
            ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
            ip_s = ip+'/24'
        except:
            ni.ifaddresses('eth0')
            ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
            ip_s = ip+'/24'

        arp_req_frame = scapy.ARP(pdst = ip_s)

        broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
        
        broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

        answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
        result = []

        for i in range(0,len(answered_list)):
            bot = answered_list[i][1].psrc
            result.append(bot)

        return result
    
    def display_result(result):
        print('List bot:\n')
        for i in result:
            print(i)
    
i = Scanbot.scan()   
for t in i:
    print(t)