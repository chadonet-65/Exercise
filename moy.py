"""
pour calculer la myen de trois nbre

"""
"""def moyenne(n1, n2, n3):
    result = (n1+n2+n3)/3
    return result"""

def moyenne(my_list=[]):
    result=0
    i = 0
    while len(str(my_list)) <= 3:
        n1 = int(input("Saissir n1 : "))
        my_list = n1
        i = i+1
    return my_list
    for i in range(len(my_list)):
        if i > len(my_list):
            print("Trop long!!!")
        result = my_list[i] / 3
    return result

if __name__ =='__main__':
   print(moyenne())