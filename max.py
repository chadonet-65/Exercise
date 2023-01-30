
def max_nbre(tab = []):
    x = tab[0]
    for n in range(len(tab)):
        if x < tab[n]:
            x = tab[n]
    return x
if __name__ == '__main__':

    tab = [2,4,8,1,8,7]
    print(max_nbre(tab))