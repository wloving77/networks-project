# Guide for Setting Up Packet Counting with Timing Telemetry in Mininet

## Step 1: Start the Mininet Simulation

# Run the network setup script using:
# This command spins up the Mininet simulation with your specified topology.
sudo python3 network_p4.py


## Step 2: Execute Packet Counting on `h1`

# Inside the Mininet CLI, start the packet counting scripts on `h1` by executing:
# This script runs two Python programs on `h1`:
# - One that performs basic packet counting.
# - Another that calculates the timing of each packet counting operation.
mininet> h1 ./h1_packet_counting.sh


## Step 3: Set Up Real-Time Monitoring

# Open two separate terminals on your machine.
# Navigate to the directory where the output files are stored:
cd network-project/testing/packet_counting_p4/tmp/


# In each terminal, monitor the output files in real-time by running the following commands:

# Terminal 1: Monitor packet counting latency
tail -f h1_packet_counting_latency.txt

# Terminal 2: Monitor packet counting output
tail -f h1_packet_counting_output.txt


## Step 4: Generate Traffic for Testing

# Back in the Mininet CLI, execute the following command to generate traffic:
# This command sends a ping from `h2` to `h1` every 0.5 seconds.
mininet> h2 ping -i 0.5 h1


# Expected Result:
# You should now see both flavors of the telemetry data writing to the respective text files,
# which are displayed in both terminal windows.
