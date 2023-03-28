
from connection import Neo4jConnection

class Node:
    def __init__(self, title):
        self.title = title
        self.type = None
        self.name = None
        self.topo = None
    
    def exists(self):
        conn = Neo4jConnection(uri="bolt://10.10.10.65:7687", user="neo4j", pwd="securepassword123")

        arr = [self.name, self.topo]

        records = conn.query(
            """
                match(n)
                where n.name = "{0}" and n.topo = "{1}"
                return n
            """.format(*arr)
        )

        data = [r.data() for r in records]

        if len(data) > 0:
            return True

        return False

    def nodeToTopo(self):

        if self.topo == None or self.name == None or self.type == None:
            print("n1, n1 type, and topo have to be set for this action")
            return

        if self.exists():
            print(self.name, " already exists")
            return

        conn = Neo4jConnection(uri="bolt://10.10.10.65:7687", user="neo4j", pwd="securepassword123")

        arr = [self.name, self.topo, self.type]

        conn.query(
            """
                match(t:topo)
                where t.name = "{1}"
                create(n:{2} {{name: "{0}", topo: "{1}", type: "{2}"}})
                create(n)-[:rel]->(t)
            """.format(*arr)
        )

        print(self.name, " created and linked to ", self.topo)

    def setName(self, name):
        self.name = name
        print(self.title, " ---> ", self.name)

    def setType(self, type):
        if type != "switch" and type != "host":
            print("switch or host are the only allowed types")
            return
        self.type = type
        print(self.title, "type ---> ", self.type)

    def show(self):
        print(self.title, "| name:", self.name, ", type:", self.type)
        # print(self.title, "type => ", self.type)
    