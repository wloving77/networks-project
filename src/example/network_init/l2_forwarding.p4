/* Simple P4 program for Layer 2 forwarding */

#include <core.p4>
#include <v1model.p4>

/* Define Ethernet header */
header ethernet_t {
    bit<48> dstAddr;
    bit<48> srcAddr;
    bit<16> etherType;
}

/* Define metadata (empty in this simple example) */
struct metadata_t { }

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

    /* Actions */
    action forward(bit<9> port) {
        standard_metadata.egress_spec = port;
    }

    action flood() {
        // Use multicast group for flooding
        standard_metadata.mcast_grp = 1; // Multicast group ID 1
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
        mac_table.apply();
    }
}

/* Egress Control (with apply block added) */
control MyEgress(inout headers_t hdr,
                 inout metadata_t meta,
                 inout standard_metadata_t standard_metadata) {
    apply {
        // No actions in this simple example
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
