class Tools:
    def __init__(self):
        self.outil = []

    def ajouter(self, tool):
        self.outil.append(tool)

    def enlever(self, tool):
        index = self.outil.index(tool)
        del self.outil[index]
    def display(self):
        print(self.outil)