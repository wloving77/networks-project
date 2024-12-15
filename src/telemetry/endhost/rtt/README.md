# Steps to Setup RTT Endhost Testing:

1. Execute `cd network_init` and execute `sudo python3 network.py`
2. In the mininet console execute `h1 python3 ./endhost_scripts/rtt.py`
3. Check `tmp/rtt_execution_time.txt` and you should see 5 executions for 200 packets