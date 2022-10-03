from cmath import inf
from webbrowser import get
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from tugBoat import getAll, getConnections

topo = "topo1"

def emptyNet():
    net = Mininet(controller=Controller)

    info("Adding Controller...")
    net.addController('c0')
    info("Adding hosts...")
    nodes = []
    print(getAll(topo))
    for x in getAll(topo):
        if x['type'] == "host":
            host = net.addHost(x['name'])
            nodes.append(host)
        elif x['type'] == "switch":
            switch = net.addSwitch(x['name'])
            nodes.append(switch)

    info("Create links...")

    for x in nodes:
        connections = getConnections(topo, x.name)
        # print(connections)
        for y in connections:
            for k in nodes:
                if k.name == y['name']:
                    net.addLink(x, k)
                

    info("start network...")
    net.start()

    info("start cli")
    CLI(net)

    info("stopping...")

    net.stop()

setLogLevel("info")
emptyNet()
