for i in {1..15}
do
    python3 ../rtt/endhost_scripts/rtt.py >> ../results/rtt_execution_time.txt 
done

for i in {1..15}
do
    python3 ../packet_counting/endhost_scripts/packet_counting.py >> ../results/packet_counting_execution_time.txt 
done

for i in {1..15}
do
    python3 ../jitter/endhost_scripts/jitter.py >> ../results/jitter_execution_time.txt 
done