import subprocess
import time


def count_packets(dst_ip, num_samples=200):
    """
    Counts packets by sending ICMP pings to a destination host.

    Args:
        dst_ip (str): IP address of the destination host (e.g., '10.0.0.2').
        num_samples (int): Number of packets to send.

    Returns:
        int: The total number of successfully sent packets.
    """
    packet_count = 0

    for i in range(num_samples):
        try:
            # Send a single ICMP ping
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", dst_ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.returncode == 0:
                # Increment packet count on successful ping
                packet_count += 1
            else:
                print(f"Ping {i + 1} failed.")
        except Exception as e:
            print(f"Error during ping {i + 1}: {e}")

    return packet_count


def time_packet_counting(dst_ip, num_samples=200):
    """
    Times the execution of the packet counting application.

    Args:
        dst_ip (str): IP address of the destination host (e.g., '10.0.0.2').
        num_samples (int): Number of packets to count.

    Returns:
        tuple: Total execution time in milliseconds and the total packet count.
    """
    # Start timing
    start_time = time.time()

    # Perform packet counting
    packet_count = count_packets(dst_ip, num_samples)

    # End timing
    end_time = time.time()

    # Calculate total execution time in milliseconds
    execution_time = (end_time - start_time) * 1000

    return execution_time, packet_count


def main():
    # Target IP address
    dst_ip = "10.0.0.2"

    # Number of samples
    num_samples = 200

    # Time the packet counting process
    execution_time, packet_count = time_packet_counting(dst_ip, num_samples)

    # Print results
    # print(f"Total Packets Counted: {packet_count}")
    print(f"Total Execution Time for {num_samples} Packets: {execution_time:.2f} ms")


if __name__ == "__main__":
    main()
