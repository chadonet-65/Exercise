
def func(tab = [],n=0,m=0):

    i = 0
    while i < tab[n]:
        if str(m) == str(tab[n]):
            return 1
        i = i+1
    return 0


if __name__ == '__main__':

    tab = [2,4,8,1,8,7,96]
    m = 8
    n=6
    print(func(tab,n,m))