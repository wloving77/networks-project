from scapy.all import sniff, conf
from datetime import datetime

# Initialize packet counter and list to store processing times
packet_count = 0
processing_times = []

conf.verb = 0


# Wrapper function to calculate processing time
def timing_wrapper(func):
    def wrapper(packet):
        global packet_count, processing_times  # Ensure we use the global counter and list

        # Start timing before processing
        start_time = datetime.now()
        func(packet)  # Process the packet
        # End timing after processing
        end_time = datetime.now()

        # Calculate and store the processing time
        process_time = (end_time - start_time).total_seconds()
        processing_times.append(process_time)

        # Increment the packet counter
        packet_count += 1

        # If 200 packets are processed, calculate the total time
        if packet_count == 200:
            total_time = sum(processing_times)
            print(
                f"Total processing time for 200 packets: {total_time:.6f} seconds",
                flush=True,
            )
            packet_count = 0

        return packet  # Ensure the packet is returned

    return wrapper


# Original packet processing function
def packet_callback(packet):
    # Placeholder function to demonstrate packet processing
    pass  # Add any custom processing logic here


def main():
    # Wrap the packet_callback function with timing_wrapper
    timed_packet_callback = timing_wrapper(packet_callback)

    # Start sniffing packets on the h1-eth0 interface using the timed callback
    # Ensure the interface name is correct for your environment
    try:
        sniff(iface="h1-eth0", prn=timed_packet_callback, store=0)
    except KeyboardInterrupt:
        # Gracefully handle the exit after 200 packets
        print("Sniffing stopped after processing 200 packets.", flush=True)


if __name__ == "__main__":
    main()
