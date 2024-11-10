from scapy.all import sniff

# Callback function to confirm packet receipt
def packet_callback(packet):
    print("Packet received", flush=True)

# Start sniffing on h1-eth0 interface
sniff(iface="h1-eth0", prn=packet_callback, store=0)
