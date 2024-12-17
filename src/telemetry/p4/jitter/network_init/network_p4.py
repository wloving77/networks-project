from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Add P4 switch and set up P4 program
net.addP4Switch("s1")

net.setP4CliInput("s1", "s1-commands.txt")

# Add hosts
net.addHost("h1")
net.addHost("h2")
net.addHost("h3")
net.addHost("h4")

# load source p4 file
net.setP4Source("s1", "l2_forwarding_jitter.p4")

# Add links
net.addLink("s1", "h1")
net.addLink("s1", "h2")
net.addLink("s1", "h3")
net.addLink("s1", "h4")

net.setIntfMac("h1", "s1", "00:00:00:00:00:01")
net.setIntfMac("h2", "s1", "00:00:00:00:00:02")
net.setIntfMac("h3", "s1", "00:00:00:00:00:03")
net.setIntfMac("h4", "s1", "00:00:00:00:00:04")


# Bandwidth setting for all links
net.setBwAll(5)

# Enable packet capture and logging
net.enablePcapDumpAll()
net.enableLogAll()

# Enable CLI and start the network
net.enableCli()
net.startNetwork()
