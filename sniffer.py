from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def process_packet(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        # Extract IP layer information
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine the protocol and display appropriate info
        if protocol == 6:  # TCP
            protocol_name = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"TCP Packet: {ip_src}:{sport} -> {ip_dst}:{dport}")
        
        elif protocol == 17:  # UDP
            protocol_name = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"UDP Packet: {ip_src}:{sport} -> {ip_dst}:{dport}")
        
        elif protocol == 1:  # ICMP
            protocol_name = "ICMP"
            print(f"ICMP Packet: {ip_src} -> {ip_dst}")
        
        else:
            protocol_name = "Other"
            print(f"Other IP Packet: {ip_src} -> {ip_dst}, Protocol: {protocol_name}")

def start_sniffing(interface=None):
    if interface:
        sniff(iface=interface, prn=process_packet, store=False)
    else:
        sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    # If you want to specify an interface, pass it to the function
    # Example: start_sniffing("eth0")
    start_sniffing()
