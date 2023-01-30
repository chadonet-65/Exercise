class Screw:
    MAX_TIGHTNESS = 5

    def __init__(self):
        self.tightness = 0

    def loosen(self):
        if self.tightness > 0:
            self.tightness -= 1
    def tighten(self):
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1
    def __str__(self):
        return "Vis avec un serrage de {}".format(self.tightness)