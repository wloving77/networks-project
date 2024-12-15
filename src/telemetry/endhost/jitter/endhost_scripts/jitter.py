import subprocess
import time


def measure_jitter(dst_ip, num_samples=10):
    """
    Measures network jitter to a destination host using ICMP ping.

    Args:
        dst_ip (str): IP address of the destination host (e.g., '10.0.0.2').
        num_samples (int): Number of RTT samples to collect.

    Returns:
        tuple: A list of jitter values in milliseconds and the average jitter.
    """
    rtt_samples = []

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

    # Filter out None values
    rtt_samples = [r for r in rtt_samples if r is not None]

    # Calculate jitter (absolute differences between consecutive RTTs)
    jitter_values = [
        abs(rtt_samples[i] - rtt_samples[i - 1]) for i in range(1, len(rtt_samples))
    ]

    # Calculate average jitter
    avg_jitter = sum(jitter_values) / len(jitter_values) if jitter_values else 0

    return jitter_values, avg_jitter


def time_jitter_application(dst_ip, num_samples=10):
    """
    Times the execution of the jitter measurement application.

    Args:
        dst_ip (str): IP address of the destination host (e.g., '10.0.0.2').
        num_samples (int): Number of RTT samples to collect.

    Returns:
        tuple: Total execution time (ms), list of jitter values (ms), and average jitter (ms).
    """
    # Start timing
    start_time = time.time()

    # Measure jitter
    jitter_values, avg_jitter = measure_jitter(dst_ip, num_samples)

    # End timing
    end_time = time.time()

    # Calculate total execution time in milliseconds
    execution_time = (end_time - start_time) * 1000

    return execution_time, jitter_values, avg_jitter


def main():
    # Target IP address (replace with the actual destination IP in your network)
    dst_ip = "10.0.0.2"

    # Number of samples
    num_samples = 200

    # Run the jitter measurement and timing
    execution_time, jitter_values, avg_jitter = time_jitter_application(
        dst_ip, num_samples
    )

    # Print results
    # print(f"\nJitter Results:")
    # for i, jitter in enumerate(jitter_values):
    #     print(f"Jitter Sample {i + 1}: {jitter:.2f} ms")

    print(f"\nAverage Jitter: {avg_jitter:.2f} ms")
    print(f"Total Execution Time: {execution_time:.2f} ms")


if __name__ == "__main__":
    main()
