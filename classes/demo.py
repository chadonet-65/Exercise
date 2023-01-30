class Demo:
    demo = 0
    def __init__(self, name):
        self.name = name

    Demo.demo += 1
    def hey(self):
        print("Hello are you Mr ",self.name)


