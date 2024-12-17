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
    bit<48> ingress_ts;       // Timestamp at ingress
    bit<48> egress_ts;        // Timestamp at egress
    bit<48> rtt;              // Round-Trip Time (RTT)
    bit<48> jitter;           // Jitter (RTT difference)
    bit<48> latency;          // Latency (execution time)
    bit<32> index;            // Index for telemetry
    bit<1> is_mirrored;       // Flag to mark mirrored packets
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

/* Ingress Control */
control MyIngress(inout headers_t hdr,
                  inout metadata_t meta,
                  inout standard_metadata_t standard_metadata) {

    /* Actions */
    action record_ingress_timestamp() {
        meta.ingress_ts = standard_metadata.ingress_global_timestamp;
        meta.is_mirrored = 1;  // Mark the packet as mirrored
    }

    action forward(bit<9> port) {
        standard_metadata.egress_spec = port;
    }

    action flood() {
        standard_metadata.mcast_grp = 1;
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
            record_ingress_timestamp();
            mac_table.apply();
        }
    }
}

/* Egress Control */
control MyEgress(inout headers_t hdr,
                 inout metadata_t meta,
                 inout standard_metadata_t standard_metadata) {

    /* Declare registers */
    register<bit<48>>(15000) rtt_register;       // Register to store RTT values
    register<bit<48>>(15000) jitter_register;    // Register to store jitter values
    register<bit<48>>(15000) latency_register;   // Register to store execution time (latency)
    register<bit<32>>(1) index_register;        // Register to track write index

    /* Actions */
    action store_telemetry(bit<32> index, bit<48> rtt, bit<48> previous_rtt, bit<48> latency) {
        // Store RTT into the RTT register
        rtt_register.write(index, rtt);

        // Calculate and store jitter (absolute difference between RTTs)
        bit<48> jitter = (rtt > previous_rtt) ? (rtt - previous_rtt) : (previous_rtt - rtt);
        jitter_register.write(index, jitter);

        // Store latency into the latency register
        latency_register.write(index, latency);
    }

    action increment_index(bit<32> current_index) {
        // Increment the index register
        index_register.write(0, current_index + 1);
    }

    apply {
        if (hdr.ethernet.isValid()) {
            // Read the current index
            index_register.read(meta.index, 0);

            if (meta.is_mirrored == 1 && meta.index < 15000) {
                // Capture egress timestamp
                meta.egress_ts = standard_metadata.egress_global_timestamp;

                // Calculate RTT
                meta.rtt = meta.egress_ts - meta.ingress_ts;

                // Calculate latency (execution time)
                meta.latency = meta.egress_ts - meta.ingress_ts;

                // Read the previous RTT value (default to 0 for first packet)
                bit<48> previous_rtt;
                bit<32> previous_index = (meta.index == 0) ? 0 : meta.index - 1;
                rtt_register.read(previous_rtt, previous_index);

                // Store telemetry: RTT, Jitter, Latency
                store_telemetry(meta.index, meta.rtt, previous_rtt, meta.latency);

                // Increment index for next telemetry write
                increment_index(meta.index);
            }
        }
    }
}

/* ComputeChecksum Control */
control MyComputeChecksum(inout headers_t hdr,
                          inout metadata_t meta) {
    apply { }
}

/* Deparser */
control MyDeparser(packet_out packet, in headers_t hdr) {
    apply {
        packet.emit(hdr.ethernet);
    }
}

/* VerifyChecksum Control */
control MyVerifyChecksum(inout headers_t hdr,
                         inout metadata_t meta) {
    apply { }
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
