class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print(f"Fichier '{self.name}'")
