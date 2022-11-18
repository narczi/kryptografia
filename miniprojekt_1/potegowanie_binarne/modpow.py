import random

def bin_exp(b, e, m):
    if m == 1:
        return 0
    else:
        r = 1
        b = b % m
        while e > 0:
            if e % 2 == 1:
                r = (r*b) % m
            b = (b*b) % m
            e = e >> 1

    return r



def fermat_test(n):
    n=int(n)
    a=random.randint(2,n-2)
    r=bin_exp(a,(n-1),n)
    if r == 1:
        return True
    else:
        return False



print(fermat_test(103))
