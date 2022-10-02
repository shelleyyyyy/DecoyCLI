

from node import Node
from decoy import Decoy

d = Decoy()

d.topo.setName("topo1")
d.n1.topo = "topo1"
d.n2.topo = "topo1"

d.topo.newTopo()

d.n1.setName("s1")
d.n1.setType("switch")

d.n1.nodeToTopo()

d.n1.type = "host"
d.n1.name = "h2"
d.n2.type = "switch"
d.n2.name = "s1"

d.linkNodes()


d.n1.type = "host"
d.n1.name = "h3"

d.linkNodes()

d.n2.type = "host"
d.n2.name = "h2"

d.linkNodes()