from cmath import inf
from webbrowser import get
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from tugboat import getAll, getConnections

# set the topo from neo4j
topo = "topo11"
# set the default gw ip/ nat ip
nat_ip = "10.0.0.69"

# def start_command(host):
#     host.cmd('/./h1_squid.sh')

def make_net():
    net = Mininet(controller=Controller)

    info("Adding Controller...\n")
    net.addController('c0')
    info("Adding hosts...\n")
    nodes = []

    for x in getAll(topo):

        default_route = "via " + nat_ip

        try:
            if x['type'] == "host":
                host = net.addHost(x['name'], defaultRoute=default_route)
                host.cmd("bash /./h1_squid.sh")
                nodes.append(host)
            elif x['type'] == "switch":
                switch = net.addSwitch(x['name'])
                nodes.append(switch)
        except:
            pass

    info("Create links...\n")

    for x in nodes:
        connections = getConnections(topo, x.name)
        for y in connections:
            for k in nodes:
                if k.name == y['name']:
                    net.addLink(x, k)
                
    net.addNAT(ip=nat_ip).configDefault()
    info("start network...\n")
    net.start()

    info("start cli\n")
    CLI(net)

    info("stopping...")

    net.stop()

setLogLevel("info")
make_net()
