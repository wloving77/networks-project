from scapy.all import sniff
from datetime import datetime

# Initialize packet counter
packet_count = 0


# Wrapper function to calculate processing time
def timing_wrapper(func):
    def wrapper(packet):
        global packet_count  # Ensure we use the global counter
        start_time = datetime.now()  # Start timing before processing
        func(packet)  # Process the packet
        end_time = datetime.now()  # End timing after processing
        process_time = (end_time - start_time).total_seconds()
        print(
            f"Time to process packet {packet_count}: {process_time:.6f} seconds",
            flush=True,
        )
        return packet  # Ensure the packet is returned

    return wrapper


# Original packet processing function
def packet_callback(packet):
    global packet_count
    packet_count += 1  # Increment the packet counter
    # print(f"Packet {packet_count} received at {datetime.now()}", flush=True)


def main():
    # Wrap the packet_callback function with timing_wrapper
    timed_packet_callback = timing_wrapper(packet_callback)

    # Start sniffing packets on the h1-eth0 interface using the timed callback
    # Ensure the interface name is correct for your environment
    sniff(iface="h1-eth0", prn=timed_packet_callback, store=0)


if __name__ == "__main__":
    main()
