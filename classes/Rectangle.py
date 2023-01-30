class Rectangle:
    def __init__(self,h, w, c="red"):
        self.h = h
        self.w = w
        self.c = c

    def area(self):
        return self.h * self.w

if __name__ == '__main__':
    rect = Rectangle(4,4)
    print(rect.area())