class Hammer:
    def __init__(self, color="red"):
        self.color = color

    def planter(self, nail):
        nail.nail_in()

    def retirer(self, nail):
        nail.remove()

    def changer(self, color):
        self.color = color

    def __repr__(self):
        return f"Marteau de couleur {self.color}"