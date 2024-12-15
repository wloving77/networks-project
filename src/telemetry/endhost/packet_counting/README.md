# Guide for Setting up Endhost Packet Counting:

1. Execute `cd network_init` and run `sudo python3 network.py` and you should have a 4 host layer 2 network being simulated.
2. Execute `h1 ../h1_packet_counting.sh` in the mininet CLI
4. Execute `cd tmp` and execute `tail -f tmp/packet_counting_exec_time.txt` to see Just the output.