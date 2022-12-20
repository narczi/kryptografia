import random
import secrets

def NWD(a,b):
    temp = 0
    while(a != b):
        if(a == 1 or b == 1):
            return 1
        elif(a > b):
            a = a - b
        elif(a < b):
            b = b - a

    if(a == b):
        return a
    elif(a > b):
        return b
    elif(b > a):
        return a

def element_odwrotny(A, M):
	m0 = M
	y = 0
	x = 1

	if (M == 1):
		return 0

	while (A > 1):
		q = A // M

		t = M

		M = A % M
		A = t
		t = y

		y = x - q * y
		x = t

	if (x < 0):
		x = x + m0

	return x


def potegowanie_binarne(b, e, m):
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
    r=potegowanie_binarne(a,(n-1),n)
    if r == 1:
        return True
    else:
        return False


def reszta_kwadratowa(prime, num):
    result = potegowanie_binarne(num, int((prime-1)/2), prime)
    if result == prime-1:
        return 0
    if result == 1:
        return 1

def losuj(podloga, sufit):
    liczba = podloga
    while(liczba < podloga + 1):
        liczba = secrets.randbelow(sufit) 

    return liczba


#GENEROWANIE KLUCZA
bity = 10
q = secrets.randbits(bity)
pierwszosc_q = test_fermata(q)
pierwszosc_p = False
licznik = 0

while(pierwszosc_q == False or pierwszosc_p == False):
    q = secrets.randbits(bity)
    pierwszosc_q = test_fermata(q)
    liczba_testow = 0
    while(pierwszosc_q == False):
            pierwszosc_q = test_fermata(q)
            liczba_testow = liczba_testow + 1
            if (liczba_testow == 30):
                    break
    licznik = licznik + 1
    p = 2 * q + 1
    pierwszosc_p = test_fermata(p)

g = losuj(1,p)
print("LOSOWANIE G PRZED PETLA:")
print("NWD(p,g) = ", NWD(p,g))
g_2 = potegowanie_binarne(g,2,p)
g_q = potegowanie_binarne(g,q,p)

print("\n")
print("### GENEROWANIE KLUCZA ###\n")
print("p =", p)
print("q =", q)
print("")
print("g =", g)
print(f"g^2 (mod p) = {g}^2 (mod {p}) = {g_2}")
print(f"g^q (mod p) = {g}^{q} (mod {p}) = {g_q}")
print("PRZED PETLA LOSOWANIA Gie")

while(NWD(p,g) != 1):
    g = losuj(1,p)

while(g_2 == 1 or g_q == 1):
    g = losuj(1,p)
    g_2 = potegowanie_binarne(g,2,p)
    g_q = potegowanie_binarne(g,q,p)
        

print("PO PETLI LOSOWANIA G")
print(f"g^2 (mod p) = {g}^2 (mod {p}) = {g_2}")
print(f"g^q (mod p) = {g}^{q} (mod {p}) = {g_q}")

x = losuj(1,p-1)

y = potegowanie_binarne(g,x,p)

print("g =", g)
print("NWD(p,g) = ", NWD(p,g))
print("x = ", x)
print("y = ", y)

#SZYFROWANIE

print("### SZYFROWANIE ###")

def encrypt(message):
    z = losuj(1,p-1)
    c_1 = potegowanie_binarne(g,z,p)
    c_2 = M * potegowanie_binarne(y,z,p)
    
    print("M = ", message)
    print("z = ", z)
    print("c_1 = ", c_1)
    print("c_2 = ", c_2)

    return {'c_1':c_1,
            'c_2':c_2}

M = 421807
encrypt(M)

#DESZYFROWANIE

print("### DESZYFROWANIE ###")

def decrypt(szyfrogram):
    c_1_inv = element_odwrotny(szyfrogram['c_1'], p)
    M_decrypt = szyfrogram['c_2'] * potegowanie_binarne(szyfrogram['c_1'], p-1-x, p) % p

    return M_decrypt

print("M_decrypt = ", decrypt(encrypt(M)))