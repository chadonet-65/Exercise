
def fun_asci(number):
    nbre = ascii(number)
    return nbre


if __name__ == '__main__':
    number = input("Saissir votre valeur : ")
    print(fun_asci(number))