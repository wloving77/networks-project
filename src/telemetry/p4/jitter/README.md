# Guide for setting up p4 enabled packet counting:

1. Run `cd network_init` and then run `sudo python3 network_p4.py` in a terminal

2. In the Mininet CLI execute `h2 ping h1 -i 0.01 -c 15000` to send 15000 pings and collect execution times

3. Run `./print_performance.sh` and it will write the performance to `results/FILENAME.txt`