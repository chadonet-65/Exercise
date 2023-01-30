def tabl(tab=[]):
    for i in range(len(tab)):
       if (i % 2) != 0:
            print(tab[i])
if __name__ == '__main__':

    tab = [2,4,8,1,8,7,96]
    tabl(tab)