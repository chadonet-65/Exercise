class Tournevis:
    def __init__(self, size=3):
        self.size = size

    def serrer(self, screw):
        screw.tighten()

    def desserrer(self, screw):
        screw.loosen()

    def __repr__(self):
        return f"Tournevis de taille {self.size}"