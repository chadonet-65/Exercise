"""
F = (9 * C)/5 + 32.
"""
def degree():
    deg = int(input("Enter degree celcuis: "))
    f = int((9 * deg)/(5+32))
    print(deg,"deg = ",f,"Fahrenheit")
if __name__ == '__main__':
    degree()