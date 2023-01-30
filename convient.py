
if __name__ == '__main__':
    nbre = float(input("Saissie nombre: "))
    """if nbre > 1 and nbre < 3:
        print("valeur ok ",nbre)
    else:
        print("Mauvaise valeur")"""
    """i = 0
    while (nbre >1 and nbre<3):
        print("valeur ok ", nbre)
        i +=1
        nbre = float(input("Saissie nombre: "))
    print("false")"""
    i=0
while (nbre < 10 or nbre > 20):
    if nbre <10:
        print("Plus petit!")
    else:
        if nbre >20:
         print("Plus grand!")
    i += 1


