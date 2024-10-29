from mininet.net import Mininet
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def simple_topology():
    # Initialize the Mininet with a default controller
    net = Mininet(controller=OVSController, link=TCLink)

    # Add the default controller
    controller = net.addController('c0')

    # Add a switch
    switch = net.addSwitch('s1')

    # Add hosts
    host1 = net.addHost('h1', ip='10.0.0.1/24')
    host2 = net.addHost('h2', ip='10.0.0.2/24')
    host3 = net.addHost('h3', ip='10.0.0.3/24')

    # Add links between the switch and each host
    net.addLink(host1, switch)
    net.addLink(host2, switch)
    net.addLink(host3, switch)

    # Start the network
    net.start()

    # Run CLI for interactive commands
    CLI(net)

    # Stop the network after exiting the CLI
    net.stop()

if __name__ == '__main__':
    # Set Mininet logging level to info
    setLogLevel('info')

    # Run the network topology
    simple_topology()
