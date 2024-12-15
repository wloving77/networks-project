for i in {1..15}
do
    python3 ../rtt/endhost_scripts/rtt.py >> ../tmp/rtt_execution_time.txt 
    python3 ../packet_counting/endhost_scripts/packet_counting.py >> ../tmp/packet_counting_execution_time.txt 
    python3 ../jitter/endhost_scripts/jitter.py >> ../tmp/jitter_execution_time.txt 
done
