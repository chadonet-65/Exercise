
def factoriel(n):
    result = 0
    i = 0
    while i <= n:
        if n ==0:
            return None
        result = i*(n-1)
        i = i+1
    return result



if (__name__ == '__main__'):
    print(factoriel(-8))