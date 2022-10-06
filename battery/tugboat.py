from neo4j import GraphDatabase

class Neo4jConnection:    
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response

def getChildren(p):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="root")

    arr = [p]

    records = conn.query(
            """
                Match(n)
                Where n.name = "{0}"
                Match(c)-[]->(n)
                return c
            """.format(*arr)
        )

    data = [r.data() for r in records]

    children = []
    for x in data:
        children.append(x['c'])

    return children

def getAll(t):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="root")

    arr = [t]

    records = conn.query(
            """
                match(n)
                where n.name = "{0}"
                match(n)-[*]-(connected)
                return distinct(connected)
            """.format(*arr)
        )

    data = [r.data() for r in records]

    children = []
    for x in data:
        children.append(x['connected'])

    return children

def getConnections(t, p):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="root")

    arr = [t, p]

    records = conn.query(
            """
                match(n)
                where n.name = "{0}"
                match(n)-[*]-(connected)
                where connected.name = "{1}"
                match(c)<-[]-(connected)
                return distinct(c)
            """.format(*arr)
        )

    data = [r.data() for r in records]

    children = []
    for x in data:
        children.append(x['c'])

    return children

