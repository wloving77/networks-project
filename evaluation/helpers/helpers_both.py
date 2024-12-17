import matplotlib.pyplot as plt


def plot_p4_vs_endhost_execution_times(telemetry_metric, p4_values, endhost_values):
    """
    Plots execution times for RTT, jitter, and packet counting.

    Args:
        rtt_times (list of float): List of execution times for RTT.
        jitter_times (list of float): List of execution times for jitter.
        packet_counting_times (list of float): List of execution times for packet counting.

    Returns:
        None: Displays the plot.
    """

    samples = list(range(1, len(p4_values) + 1))  # Generate sample indices (1 to 15)

    plt.figure(figsize=(10, 6))
    plt.plot(
        samples, p4_values, label=f"{telemetry_metric} P4", color="red", marker="o"
    )
    plt.plot(
        samples,
        endhost_values,
        label=f"{telemetry_metric} Endhost",
        color="blue",
        marker="o",
    )

    plt.title(
        f"Execution Times for 1000 Packets Comparing P4 to Endhost {telemetry_metric}"
    )
    plt.xlabel("Sample (1-15)")
    plt.ylabel("Total Execution Time for 1000 Packets (ms)")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()
