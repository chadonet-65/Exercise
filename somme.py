
def sum(tab = []):
    r = 0
    for i in range(len(tab)):
        r += tab[i]
    return r
if __name__ == '__main__':

    tab = [2,4,8,1,8,7,96,4]
    print(sum(tab))