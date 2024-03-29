from connection import Neo4jConnection

class Topo:
    def __init__(self):
        self.name = None

    def exists(self):
        conn = Neo4jConnection(uri="bolt://10.10.10.65:7687", user="neo4j", pwd="securepassword123")

        arr = [self.name]

        records = conn.query(
            """
                match(n:topo)
                where n.name = "{0}"
                return n
            """.format(*arr)
        )

        data = ""
        try:
            data = [r.data() for r in records]
        except:
            pass

        if len(data) > 0:
            return True

        return False

    def newTopo(self):
        if self.exists():
            print("This topo already exists")
            return False

        conn = Neo4jConnection(uri="bolt://10.10.10.65:7687", user="neo4j", pwd="securepassword123")

        arr = [self.name]
        conn.query(
            """
                create(s:topo {{name: "{0}", topo: "{0}"}})
            """.format(*arr)
        )
        print("created " + self.name)
        return True

    def setName(self, name):
        # if not self.exists(name):
        #     print("This topo does not exist")
        #     return

        self.name = name
        print("topo ---> ", self.name)

    def show(self):
        print("topo | ", self.name)

