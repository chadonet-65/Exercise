if __name__ =='__main__':
    """n = int(input("Saissir valeur: "))
    for i in range(1,11):
        print("{}x{} = {}".format(n,i,n*i))"""
    """while True:
        try:
            x = int(input("Please enter the number: "))
            break
        except ValueError:
            print("Oops! That was no valid")"""
    try:
        raise Exception('spam','eggs')
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)

        x, y = inst.args
        print('x= ',x)
        print('y= ',y)