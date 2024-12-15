import time
import subprocess


def measure_rtt(dst_ip, num_samples=10):
    """
    Measures RTT to a destination host using ICMP ping.

    Args:
        dst_ip (str): IP address of the destination host (e.g., '10.0.0.2').
        num_samples (int): Number of RTT samples to collect.

    Returns:
        list: A list of RTT samples in milliseconds.
    """
    rtt_samples = []
    # print(f"Pinging {dst_ip}...")

    for i in range(num_samples):
        try:
            # Execute a single ping command
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", dst_ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.returncode == 0:
                # Parse RTT from the output
                for line in result.stdout.splitlines():
                    if "time=" in line:
                        rtt = float(line.split("time=")[1].split(" ")[0])
                        rtt_samples.append(rtt)
                        break
            else:
                print(f"Ping {i + 1} failed.")
                rtt_samples.append(None)  # Append None for failed pings
        except Exception as e:
            print(f"Error during ping: {e}")
            rtt_samples.append(None)

    return [r for r in rtt_samples if r is not None]  # Filter None values


def time_rtt_application(dst_ip, num_samples=10):
    """
    Times the execution of the RTT measurement application.

    Args:
        dst_ip (str): IP address of the destination host (e.g., '10.0.0.2').
        num_samples (int): Number of RTT samples to collect.

    Returns:
        tuple: Total execution time (ms) and the list of RTT samples (ms).
    """
    # print(f"Timing RTT application to {dst_ip}...")

    # Start timing
    start_time = time.time()

    # Measure RTT
    rtt_samples = measure_rtt(dst_ip, num_samples)

    # End timing
    end_time = time.time()

    # Calculate total execution time in milliseconds
    execution_time = (end_time - start_time) * 1000

    return execution_time, rtt_samples


def main():
    # Target IP address (replace with the actual destination IP in Mininet)
    dst_ip = "10.0.0.2"

    # Number of samples
    num_samples = 200

    # Run the RTT measurement and timing
    execution_time, rtt_samples = time_rtt_application(dst_ip, num_samples)

    # Print results
    # print("\nRTT Results:")
    # for i, rtt in enumerate(rtt_samples):
    #     print(f"Sample {i + 1}: {rtt:.2f} ms")

    # if rtt_samples:
    #     avg_rtt = sum(rtt_samples) / len(rtt_samples)
    #     print(f"\nAverage RTT: {avg_rtt:.2f} ms")

    print(f"Total Execution Time for 200 Packets: {execution_time:.2f} ms")


if __name__ == "__main__":
    main()
