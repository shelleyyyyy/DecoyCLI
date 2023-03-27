
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

topo = "topo11"

topo_decoy = {
    "type": "topo",
    "name": topo,
    "conn": [

    ],
    "children": [
        {
            "type": "switch",
            "name": "s1",
            "conn": [
                {
                    "name": topo
                },
                {
                    "name": "s3"
                },
            ],
            "children": [
                 {
                    "type": "host",
                    "name": "h1",
                    "conn": [
                        {
                            "name": "s1"
                        }
                    ],
                    "children": [
                        
                    ]
                },
                 {
                    "type": "host",
                    "name": "h2",
                    "conn": [
                        {
                            "name": "s1"
                        }
                    ],
                    "children": [
                        
                    ]
                },
                 {
                    "type": "host",
                    "name": "h3",
                    "conn": [
                        {
                            "name": "s1"
                        }
                    ],
                    "children": [
                        
                    ]
                },
            ]
        },            
        {
            "type": "switch",
            "name": "s2",
            "conn": [
                {
                    "name": topo
                },
                {
                    "name": "s1"
                }
            ],
            "children": [
                 {
                    "type": "host",
                    "name": "h4",
                    "conn": [
                        {
                            "name": "s2"
                        }
                    ],
                    "children": [
                        
                    ]
                },
                 {
                    "type": "host",
                    "name": "h5",
                    "conn": [
                        {
                            "name": "s2"
                        }
                    ],
                    "children": [
                        
                    ]
                },
                 {
                    "type": "host",
                    "name": "h6",
                    "conn": [
                        {
                            "name": "s2"
                        }
                    ],
                    "children": [
                        
                    ]
                },
            ]
        },    
    ]
}

conn = Neo4jConnection(uri="bolt://10.10.10.65:7687", user="neo4j", pwd="root")

def addNode(conn_arr, type, name, children):
    arr = [type, name, topo]

    conn.query(
        """
            Create(s:{0} {{name: "{1}", type: "{0}", topo: "{2}"}})
        """.format(*arr)
    )

    for x in conn_arr:
        arr = [x['name'], name, topo]
        conn.query(
            """
                Match(n)
                Where n.name = "{0}" and n.topo = "{2}"
                Match(s)
                Where s.name = "{1}" and s.topo = "{2}"
                Create(s)-[:rel]->(n)
            """.format(*arr)
        )

    for x in children:
        addNode(x['conn'], x['type'], x['name'], x['children'])
    
addNode(topo_decoy['conn'], topo_decoy['type'], topo_decoy['name'], topo_decoy['children'])

