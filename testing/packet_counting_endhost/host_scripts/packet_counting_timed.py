from scapy.all import sniff
from datetime import datetime

# Initialize packet counter and start time
packet_count = 0
start_time = datetime.now()

# Wrapper function to calculate processing time
def timing_wrapper(func):
    def wrapper(packet):
        start_time = datetime.now()  # Start timing before processing
        func(packet)  # Process the packet
        end_time = datetime.now()  # End timing after processing
        process_time = (end_time - start_time).total_seconds()
        print(f"Time to process packet {packet_count}: {process_time:.6f} seconds", flush=True)
    return wrapper

# Original packet processing function
def packet_callback(packet):
    global packet_count, start_time
    packet_count += 1  # Increment the packet counter

    # Print packet information (you can remove or comment this line to reduce output)
    #print(f"Packet {packet_count}: {packet.summary()}", flush=True)

    # Example telemetry calculations
    current_time = datetime.now()
    elapsed_time = (current_time - start_time).total_seconds()

    # Packet rate calculation
    packet_rate = packet_count / elapsed_time if elapsed_time > 0 else 0
    #print(f"Elapsed Time: {elapsed_time:.2f} sec, Packet Rate: {packet_rate:.2f} packets/sec", flush=True)

# Wrap the packet_callback function with timing_wrapper
timed_packet_callback = timing_wrapper(packet_callback)

# Start sniffing packets on the h1-eth0 interface using the timed callback
sniff(iface="h1-eth0", prn=timed_packet_callback, store=0)
