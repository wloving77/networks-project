from scapy.all import sniff
from datetime import datetime

# Initialize packet counter and start time
packet_count = 0
start_time = datetime.now()

# Callback function to process each packet
def packet_callback(packet):
    global packet_count
    packet_count += 1  # Increment the packet counter

    # Print packet information (you can remove or comment this line to reduce output)
    print(f"Packet {packet_count}: {packet.summary()}", flush=True)

    # Example telemetry calculations
    current_time = datetime.now()
    elapsed_time = (current_time - start_time).total_seconds()

    # Packet rate calculation
    packet_rate = packet_count / elapsed_time if elapsed_time > 0 else 0
    print(f"Elapsed Time: {elapsed_time:.2f} sec, Packet Rate: {packet_rate:.2f} packets/sec", flush=True)

# Start sniffing packets on the h1-eth0 interface
sniff(iface="h1-eth0", prn=packet_callback, store=0)
