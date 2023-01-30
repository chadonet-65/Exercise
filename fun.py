
def add():
    a = int(input("saissir nbre 1 : "))
    b = int(input("saissir nbre 2 : "))
    resul = a + b
    print("{} + {} = {}".format(a, b, resul))

def sub():
    a = int(input("saissir nbre 1 : "))
    b = int(input("saissir nbre 2 : "))
    resul = a - b
    print("{} - {} = {}".format(a, b, resul))

def mul():
    a = int(input("saissir nbre 1 : "))
    b = int(input("saissir nbre 2 : "))
    resul = a * b
    print("{} * {} = {}".format(a, b, resul))

def div():
    a = int(input("saissir nbre 1 : "))
    b = int(input("saissir nbre 2 : "))
    if b == 0:
        print("A number divide by 0 do not existed")
    resul = a / b
    print("{} / {} = {}".format(a, b, resul))