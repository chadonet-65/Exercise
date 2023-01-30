
from equation import equation
from fun import add
from sys import argv
from super import super_marche
from math import pi
comb = [[]]

"""for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            comb.append((x**2,y))
            print(comb)"""

"""[str(round(pi, i)) for i in range(1, 6)]

for i in range(1, 6):
    print(str(round(pi, i)))"""
def square_matrix_simple(matrix=[]):
    return list(map(lambda m: list(map(lambda y: y**2, m)), matrix))
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(square_matrix_simple(matrix))