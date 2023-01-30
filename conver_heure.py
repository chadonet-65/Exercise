from math import ceil
def convertir_heure():
    heure = int(input("Enter the hour: "))
    min = int(input("Enter the minutes: "))

    if(heure < 0 or min < 0):
        print("Sorry hour > 0 or minute > 0")
    else:
       cal = heure + (min/60)
       print("he is {}h{}min = {}".format(heure,min,cal))

if __name__ == '__main__':
    convertir_heure()