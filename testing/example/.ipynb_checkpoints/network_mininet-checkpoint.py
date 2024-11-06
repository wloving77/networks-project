from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
import time

def simple_topology():
    # Set up the Mininet network
    net = Mininet(switch=OVSSwitch)
    
    # Add hosts with unique IP addresses
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')
    
    # Add a single switch
    s1 = net.addSwitch('s1')
    
    # Add links between each host and the switch
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    
    # Start the network
    net.start()
    
    # Run packet counting script on h1
    h1.cmd('python3 ./host_scripts/packet_counter.py &')  # Replace with actual path to your script

    # Short delay to allow the script to start
    time.sleep(2)
    
    # Run ping tests to verify connectivity
    print("Testing network connectivity")
    net.pingAll()
    
    # Start the Mininet CLI
    CLI(net)
    
    # Stop the network after exiting CLI
    net.stop()

if __name__ == '__main__':
    # Set Mininet logging level to 'info' to see output in console
    setLogLevel('info')
    simple_topology()
