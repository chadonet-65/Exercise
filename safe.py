def safe_print_list(my_list=[], x=0):
    res = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            res += 1
        except IndexError:
            break
    print("")
    return (res)
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
def safe_print_list_integers(my_list=[], x=0):
    res = 0
    for i in range(0,x):
        try:
            print("{:d}".format(my_list[i]), end="")
            res += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (res)
def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
if __name__ == '__main__':
    my_list = [1,2,3,4,"5"]
    x=5
    safe_print_division(45,5)