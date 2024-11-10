/* Simple P4 program for Layer 2 forwarding with packet counting and latency measurement using registers */

#include <core.p4>
#include <v1model.p4>

/* Define Ethernet header */
header ethernet_t {
    bit<48> dstAddr;
    bit<48> srcAddr;
    bit<16> etherType;
}

/* Define metadata */
struct metadata_t {
    bit<48> ingress_ts;
    bit<32> latency_idx;  // Added to store the current index
}

/* Define all headers */
struct headers_t {
    ethernet_t ethernet;
}

/* Parser */
parser MyParser(packet_in packet,
                out headers_t hdr,
                inout metadata_t meta,
                inout standard_metadata_t standard_metadata) {
    state start {
        packet.extract(hdr.ethernet);
        transition accept;
    }
}

/* VerifyChecksum Control (empty in this example) */
control MyVerifyChecksum(inout headers_t hdr,
                         inout metadata_t meta) {
    apply {
        // No checksum verification in this simple example
    }
}

/* Ingress Control */
control MyIngress(inout headers_t hdr,
                  inout metadata_t meta,
                  inout standard_metadata_t standard_metadata) {

    /* Declare packet counter with size 1 */
    counter(1, CounterType.packets) c;

    /* Actions */
    action forward(bit<9> port) {
        standard_metadata.egress_spec = port;
    }

    action flood() {
        // Use multicast group for flooding
        standard_metadata.mcast_grp = 1; // Multicast group ID 1
    }

    action tally() {
        // Increment the counter at index 0
        c.count(0);
    }

    /* Match-Action Table */
    table mac_table {
        key = {
            hdr.ethernet.dstAddr: exact;
        }
        actions = {
            forward;
            flood;
        }
        size = 1024;
        default_action = flood();
    }

    apply {
        if (hdr.ethernet.isValid()) {
            // Capture ingress timestamp
            meta.ingress_ts = standard_metadata.ingress_global_timestamp;

            // Call tally directly for every valid packet
            tally();
        }

        // Apply the MAC table for forwarding decisions
        mac_table.apply();
    }
}

/* Egress Control */
control MyEgress(inout headers_t hdr,
                 inout metadata_t meta,
                 inout standard_metadata_t standard_metadata) {

    /* Declare registers */
    register<bit<48>>(1000) latency_register;  // Register array to store latency values
    register<bit<32>>(1) latency_index;        // Register to keep track of the current index

    /* Actions */
    action read_latency_index() {
        // Read the current index into metadata
        latency_index.read(meta.latency_idx, 0);
    }

    action store_latency() {
        // Capture egress timestamp
        bit<48> egress_ts = standard_metadata.egress_global_timestamp;

        // Compute latency
        bit<48> latency = egress_ts - meta.ingress_ts;

        // Write latency to the register array at the current index
        latency_register.write(meta.latency_idx, latency);

        // Increment the index and write it back
        latency_index.write(0, meta.latency_idx + 1);
    }

    apply {
        if (hdr.ethernet.isValid()) {
            // Read the current index
            read_latency_index();

            // Only store latency if index < 1000
            if (meta.latency_idx < 1000) {
                // Store latency into the register array
                store_latency();
            }
            // Else, do nothing (stop storing latency values)
        }
    }
}

/* ComputeChecksum Control (empty in this example) */
control MyComputeChecksum(inout headers_t hdr,
                          inout metadata_t meta) {
    apply {
        // No checksum computation in this simple example
    }
}

/* Deparser */
control MyDeparser(packet_out packet, in headers_t hdr) {
    apply {
        packet.emit(hdr.ethernet);
    }
}

/* Instantiate the architecture */
V1Switch(
    MyParser(),
    MyVerifyChecksum(),
    MyIngress(),
    MyEgress(),
    MyComputeChecksum(),
    MyDeparser()
) main;
