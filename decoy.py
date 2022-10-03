from connection import Neo4jConnection
from node import Node
from topo import Topo

class Decoy:
    def __init__(self):
        self.topo = Topo()
        self.n1 = Node("n1")
        self.n2 = Node("n2")

    def showOptions(self):
        print("set topo <topo name> --sets topo")
        print("set n1 <node name> --sets node 1 can be new or existing")
        print("set n2 <node name> --sets node 2 must be existing")
        print("create topo --generates new topo node in db")
        print("create n1 n2 --generates n1 in db and connects to n2")
        print("create n1 topo --generates n1 in db and connects to topo")
        print("kill n1 --deletes n1 in db")
        print("kill n2 --deletes n2 in db")
        print("kill topo --deletes topo in db")

    def show(self):
        self.topo.show()
        self.n1.show()
        self.n2.show()

    def linkExisting(self):
        conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="root")

        arr = [self.topo.name, self.n1.name, self.n2.name]

        conn.query(
            """
                match(n:topo)
                where n.name = "{0}"
                match(n)-[*]-(c)
                where c.name = "{1}"
                match(i:topo)
                where i.name = "{0}"
                match(i)-[*]-(k)
                where k.name = "{2}"
                create(c)-[:rel]->(k)
            """.format(*arr)
        )

        print("created link from ", self.n1.name, " to ", self.n2.name)

    def genAndLink(self):
        conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="root")

        arr = [self.topo.name, self.n1.name, self.n1.type, self.n2.name]

        conn.query(
            """
                match(n:topo)
                where n.name = "{0}"
                match(n)-[*]-(c)
                where c.name = "{3}"
                create(h:host {{name: "{1}", type: "{2}", topo: "{0}"}})
                create(h)-[:rel]->(c)
            """.format(*arr)
        )

        print("created ", self.n1.name, " and linked to ", self.n2.name)

    def linkNodes(self):
        if self.n2.exists():
            if self.n1.exists():
                self.linkExisting()
            else:
                self.genAndLink()
        else: 
            print("n2 must already be created in db")


    def start(self):
        while True:
            a = input('decoy> ')

            res = a.split()
            # print("\n")
            if res[0] == "show":
                self.show()
            elif res[0] == "set":
                if res[1] == "n1":
                    if res[2] == "name":
                        self.n1.setName(res[3])
                    elif res[2] == "type":
                        self.n1.setType(res[3])
                elif res[1] == "n2":
                    if res[2] == "name":
                        self.n2.setName(res[3])
                    elif res[2] == "type":
                        self.n2.setType(res[3])
                elif res[1] == "topo":
                    self.topo.setName(res[2])
                    self.n1.topo = res[2]
                    self.n2.topo = res[2]
                else:
                    print(res[1], " is not a node")
            elif res[0] == "create":
                if res[1] == "topo":
                    self.topo.newTopo()
                elif res[1] == "n1":
                    if res[2] == "topo":
                        if not self.topo.exists():
                            print("The set topo does not exist")
                        else:
                            self.n1.nodeToTopo()
                    elif res[2] == "n2":
                        self.linkNodes()


            elif res[0] == "help":
                self.showOptions()

            # print("\n")
    

