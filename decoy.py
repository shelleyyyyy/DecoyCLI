from genericpath import exists
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
        print("set n1 <node name> --sets node 1")
        print("set n2 <node name> --sets node 2")
        print("create topo --generates new topo node in db")
        print("create n1 --generates new node in db")
        print("kill n1 --deletes node in db")
        print("kill topo --deletes topo in db")
        print("link --creates link between set nodes")

    def show(self):
        self.topo.show()
        self.n1.show()
        self.n2.show()

    def start(self):
        while True:
            a = input('decoy> ')

            res = a.split()
            
            if res[0] == "show":
                self.show()
            elif res[0] == "set":
                if res[1] == "n1":
                    self.n1.setName(res[2])
                elif res[1] == "n2":
                    self.n2.setName(res[2])
                elif res[1] == "topo":
                    self.topo.setName(res[2])
                else:
                    print(res[1], " is not a node")
            elif res[0] == "create":
                if res[1] == "topo":
                    self.topo.newTopo()
            elif res[0] == "help":
                self.showOptions()
    
t = Decoy()

t.start()

