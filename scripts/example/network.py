from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()


net.addP4Switch('s1')
net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')

net.addLink('s1', 'h1')
net.addLink('s1', 'h2')
net.addLink('s1', 'h3')
net.addLink('s1', 'h4')

# net.setIntfPort('s1', 'h1', 1)  # Set the number of the port on s1 facing h1
# net.setIntfPort('h1', 's1', 0)  # Set the number of the port on h1 facing s1
# net.setIntfPort('s1', 'h2', 2)  # Set the number of the port on s1 facing h2
# net.setIntfPort('h2', 's1', 0)  # Set the number of the port on h2 facing s1
# net.setIntfPort('s1', 'h3', 3)  # Set the number of the port on s1 facing h3
# net.setIntfPort('h3', 's1', 0)  # Set the number of the port on h3 facing s1
# net.setIntfPort('s1', 'h4', 4)  # Set the number of the port on s1 facing h4
# net.setIntfPort('h4', 's1', 0)  # Set the number of the port on h4 facing s1

net.setBwAll(5)

net.l3()

net.enablePcapDumpAll()
net.enableLogAll()

net.enableCli()
net.startNetwork()