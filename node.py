
class Node:
    def __init__(self, title):
        self.title = title
        self.name = None

    def setName(self, name):
        self.name = name
        print(self.title, " ---> ", self.name)

    def show(self):
        print(self.title, "=>", self.name)
    