import matplotlib.pyplot as plt


def extract_numbers_from_file(file_path):
    """
    Extracts numbers from lines in a file containing execution times.

    Args:
        file_path (str): Path to the .txt file.

    Returns:
        list: A list of extracted numbers as floats.
    """
    numbers = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Split the line and extract the last part as the number
                try:
                    number = float(
                        line.split()[-2]
                    )  # Extract the second-to-last element (the number)
                    numbers.append(number)
                except ValueError:
                    print(f"Skipping line due to invalid format: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return numbers


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

    plt.title("Execution Times for 200 Packets")
    plt.xlabel("Sample (1-15)")
    plt.ylabel("Total Execution Time for 200 Packets (ms)")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()
