
def sum(n):
    r = 0
    
    while n > 0:
        r += n*n*n
        n = n - 1
    return r

if __name__ == '__main__':
    print(sum(5))