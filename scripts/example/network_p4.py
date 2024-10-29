from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Add P4 switch and set up P4 program
net.addP4Switch('s1')
net.setP4Source('s1', 'l2_learning.p4')

# Add hosts
net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')

# Add links
net.addLink('s1', 'h1')
net.addLink('s1', 'h2')
net.addLink('s1', 'h3')
net.addLink('s1', 'h4')

# Explicit port configuration
net.setIntfPort('s1', 'h1', 1)
net.setIntfPort('s1', 'h2', 2)
net.setIntfPort('s1', 'h3', 3)
net.setIntfPort('s1', 'h4', 4)

# Bandwidth setting for all links
net.setBwAll(5)

# Enable packet capture and logging
net.enablePcapDumpAll()
net.enableLogAll()

# Enable CLI and start the network
net.enableCli()
net.startNetwork()
