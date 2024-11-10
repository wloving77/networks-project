# Guide for setting up p4 enabled packet counting:

1. Run `sudo python3 network_p4.py` in a terminal

2. Run `simple_switch_CLI --thrift-port 9090` in another terminal

3. Run `h1 ping h2` in the first `mininet` terminal

4. Run `register_read latency_register` in the `thrift` terminal

5. Everytime you rerun the comman in **4** you should see more latency values in nanoseconds.