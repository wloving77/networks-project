#sudo python3 host_scripts/packet_counter.py > tmp/h1_packet_counting_output.txt &
sudo python3 ../endhost_scripts/packet_counting_timed.py > ../tmp/packet_counting_exec_time.txt &
sudo python3 ../endhost_scripts/total_execution.py > ../tmp/total_execution.txt &

