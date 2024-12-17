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


import matplotlib.pyplot as plt


def plot_telemetry_comparison(end_host, p4, pim, metric_name="Telemetry Metric"):
    """
    Generate a bar plot comparing average execution times for End-Host, P4, and PIM.

    Parameters:
    - end_host (int or float): Value for End-Host.
    - p4 (int or float): Value for P4.
    - pim (int or float): Value for PIM.
    - metric_name (str): Title of the plot representing the telemetry metric.
    """
    # Define labels, values, and colors
    labels = ["End-Host", "P4", "PIM"]
    values = [end_host, p4, pim]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]  # Blue, Orange, Green

    # Create the bar plot
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=colors)

    # Add title and labels
    plt.title(f"{metric_name} Average Comparison", fontsize=14)
    plt.ylabel("Execution Time (ms)", fontsize=12)
    plt.xlabel("Computation Method", fontsize=12)

    # Display values on top of bars
    for i, value in enumerate(values):
        plt.text(
            i, value + 0.05 * max(values), f"{value:.2f}", ha="center", fontsize=10
        )

    # Show the plot
    plt.tight_layout()
    plt.show()
