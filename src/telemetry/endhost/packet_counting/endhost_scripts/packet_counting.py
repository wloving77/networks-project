import subprocess
import time


def perform_ping(dst_ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", dst_ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    return result


def count_packets(ping_results):
    """
    Counts packets by sending ICMP pings to a destination host.

    Args:
        dst_ip (str): IP address of the destination host (e.g., '10.0.0.2').
        num_samples (int): Number of packets to send.

    Returns:
        int: The total number of successfully sent packets.
    """
    packet_count = 0
    for ping_result in ping_results:
        try:
            if ping_result.returncode == 0:
                # Increment packet count on successful ping
                packet_count += 1

            else:
                print(f"Pingfailed.")
        except Exception as e:
            print(f"Error during ping: {e}")

    return packet_count


def main():
    # Target IP address
    dst_ip = "10.0.0.2"

    # Number of samples
    num_samples = 1000
    ping_results = []

    for i in range(num_samples):
        ping_result = perform_ping(dst_ip)
        ping_results.append(ping_result)

    # Time the packet counting process

    start_time = time.time()
    packet_count = count_packets(ping_results)
    end_time = time.time()

    # Calculate total execution time in milliseconds
    execution_time = (end_time - start_time) * 1000

    # Print results
    # print(f"Total Packets Counted: {packet_count}")
    print(f"Total Execution Time for {num_samples} Packets: {execution_time:.2f} ms")


if __name__ == "__main__":
    main()
