import secrets
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

def test_fermata(n):
    n=int(n)
    a=random.randint(2,n-2)
    r=bin_exp(a,(n-1),n)
    if r == 1:
        return True
    else:
        return False


bity = 500

def is_prime(num, tests):
    for i in range(1, tests + 1):
        pierwszosc_num = test_fermata(num)
        if(pierwszosc_num == False):
            break
    return pierwszosc_num

def generate_prime(tests):
    pierwszosc_q = False
    while(pierwszosc_q == False):
        q = secrets.randbits(bity)
        pierwszosc_q = is_prime(q, tests)
    return q
    
def pq(tests):
    q = generate_prime(tests)
    p = 2 * q + 1
    while(is_prime(q, tests) != True or is_prime(p, tests) != True):
        q = generate_prime(tests)
        p = 2 * q + 1
        if(is_prime(p, tests) == True):
            return p, q
        else:
            continue

p, q = pq(1)
print(p)
print(q)
