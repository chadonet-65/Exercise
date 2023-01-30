
def lendemain():
    jr = int(input("Enter the day: "))
    mois = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    if (jr <= 0 or mois <= 0 or year <= 0 or year < 1582 or mois > 12):
        print("Date don't valide")
    else:
        if jr >= 31:
            jr = 1
            if mois >= 1 and mois < 12:
                mois +=1
            elif mois == 12:
               year += 1
               mois = 1
            else:
                mois = 1
        else:
            jr +=1
    print(jr,"/",mois,"/",year)

if __name__ == '__main__':
    lendemain()