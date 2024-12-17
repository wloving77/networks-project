#!/bin/bash

# Script to read latency_register and save the output to a file

# Variables
THRIFT_PORT=9090
LATENCY_REGISTER="latency_register"
OUTPUT_FILE="results/latency_results_packet_counting.txt"

# Inform user
echo "Reading ${LATENCY_REGISTER} from Thrift CLI and saving results to ${OUTPUT_FILE}..."

# Execute Thrift CLI command and save output to a file
simple_switch_CLI --thrift-port ${THRIFT_PORT} << EOF > ${OUTPUT_FILE}
register_read ${LATENCY_REGISTER}
EOF

# Confirm completion
echo "Results saved to ${OUTPUT_FILE}."
