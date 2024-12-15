for i in {1..5}
do
    python3 ../packet_counting/endhost_scripts/packet_counting.py >> ../tmp/packet_counting_execution_time.txt 
done
