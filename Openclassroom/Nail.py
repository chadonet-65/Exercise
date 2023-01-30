class Nail:
    def __init__(self):
        self.in_wall = False

    def nail_in(self):
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"clou {wall_state}"