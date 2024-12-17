import matplotlib.pyplot as plt
import re


def parse_latency_file(file_path):
    latency_values = []

    # Define regex to find "latency_register=" and capture the following numbers
    pattern = r"latency_register=\s*([\d,\s]+)"

    with open(file_path, "r") as file:
        content = file.read()

    # Search for the latency_register= pattern
    match = re.search(pattern, content)
    if match:
        # Extract values and split by comma
        raw_values = match.group(1).split(",")
        latency_values = [
            int(value.strip()) / 1000000
            for value in raw_values
            if value.strip().isdigit()
        ]
    else:
        print("No latency_register values found in the file.")

    return latency_values


def chunk_by_1000(latency_values):
    result_list = []
    intermediate_sum = 0
    for i in range(0, 15001):
        if i % 1000 == 0 and i != 0:
            result_list.append(intermediate_sum)
            intermediate_sum = 0
            continue
        intermediate_sum += latency_values[i]
    return result_list


def plot_endhost_execution_times(rtt_times, jitter_times, packet_counting_times):
    """
    Plots execution times for RTT, jitter, and packet counting.

    Args:
        rtt_times (list of float): List of execution times for RTT.
        jitter_times (list of float): List of execution times for jitter.
        packet_counting_times (list of float): List of execution times for packet counting.

    Returns:
        None: Displays the plot.
    """
    if not (len(rtt_times) == len(jitter_times) == len(packet_counting_times)):
        print("All lists must have the same length.")
        return

    samples = list(range(1, len(rtt_times) + 1))  # Generate sample indices (1 to 15)

    plt.figure(figsize=(10, 6))
    plt.plot(samples, rtt_times, label="RTT", color="red", marker="o")
    plt.plot(samples, jitter_times, label="Jitter", color="blue", marker="o")
    plt.plot(
        samples,
        packet_counting_times,
        label="Packet Counting",
        color="green",
        marker="o",
    )

    plt.title("Execution Times for 1000 Packets in P4")
    plt.xlabel("Sample (1-15)")
    plt.ylabel("Total Execution Time for 1000 Packets (ms)")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()
