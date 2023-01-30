"""
Ax2 + Bx + C = 0
del = b*b - 4*A*C
 si del < 0 alors  equation ne peut etre resolus
 si del = 0 alors x = -B/2*A
 si del > 0 alors x1 = -B - del / 2A, x2 = -B + del/2A
"""
from math import *

def equation():
    global a
    a=98
    A = int(input("Enter value A : "))
    B = int(input("Enter value B : "))
    C = int(input("Enter value C : "))
    print("Equation a resoudre {}X2 + {}X + {} = 0".format(A,B,C))
    delta =(B*B-4*A*C)
    if delta < 0:
          print("Delta vaut : {} ".format(delta))
          print("Impossible de calculer la racine carrée d'un nombre negatif")
    elif delta == 0:
        x1 = (-B/(2 * A))
        print("Delta vaut : {} ".format(delta))
        print("La solution est de: {}".format(x1))
    else:
         rc = sqrt(delta)
         x1 = ((-B-rc)/(A * 2))
         x2 = ((-B+rc)/(A * 2))
         print("Delta vaut : {} et sa racine carré vaut : {}".format(delta, rc))
         print("Solution : [{},{}]".format(x1,x2))
