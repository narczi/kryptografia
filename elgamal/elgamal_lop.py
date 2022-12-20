import numpy as np
#1
def obliczanie_odwrotności(n, b):  #z = b^(-1) mod n
    x = b
    y = n
    u = 0
    v = 1
    while True:
        q = x // y

        ab_matrix = np.array([[0, 1], [1, -q]]) @ np.array([[x], [y]])
        uv_matrix = np.array([[0, 1], [1, -q]]) @ np.array([[u], [v]])
        x, y, u, v = ab_matrix[0][0], ab_matrix[1][0], uv_matrix[0][0], uv_matrix[1][0]
        if y == 0:
            break
    b_inv = (x - n * u) // b 
    return b_inv

#2
def efektywne_potegowanie(n, k, b):  # y=b^k mod n
    k = int(k)
    y = 1
    i = k.bit_length()
    while i >= 0:
        ki = (k >> i) & 1
        y = y ** 2 % n
        if ki == 1:
            y = y * b % n
        i = i - 1
    return y

#3 
import random
 
def czy_n_jest_liczbą_pierwszą(k, n):    #k- określa dokładność testu, n - liczba do sprawdzenia, test Fermata
    i = 0
    while i < k:
        a = random.randint(1, n - 1)
        if pow(a, (n - 1), n) == 1:
            i = i + 1
        else:
            return False
 
    return True

#4
def czy_jest_resztą_kwadratową(p, b):   # p-liczba pierwsza, b-reszta kwadratowa, twierdzenie Eulera
    if efektywne_potegowanie(p, (p - 1) / 2, b) == 1:
        return True
    else:
        return False

#5
def pierwiastek_kwadratowy(p, b):     # b-reszta kwadratowa, twierdzenie Eulera
    return efektywne_potegowanie(p, (p + 1) / 4, b)

def random_pq():
    k = 30
    bits = 50
    
    while True:
        q = random.getrandbits(bits)                        
        a = czy_n_jest_liczbą_pierwszą(k,q)             
        #print(q, a)
        if a == True:
            break     
            
    p = 2*q + 1
    #print("p",p)
    b = czy_n_jest_liczbą_pierwszą(k,p)                  
    
    if b == 1:                                          
        #print("p",p)
        #print("p",p)
        return p, q
    
    else:                                                
        return random_pq()
    
print(random_pq())

def pq():
    p = 120471683029418687071538440325434591814539544830974289094629223908748885878701977499366767041636724573600462526018305751410401637006900776611105633028708553943579675496053770805388766680786652129988323
    q = 60235841514709343535769220162717295907269772415487144547314611954374442939350988749683383520818362286800231263009152875705200818503450388305552816514354276971789837748026885402694383340393326064994161
    g = 49715514348199090400843794814660308877056073622245224797010955964356803526998184663309372595341717728544108806549188510677381031650589317444134306192256169850270129536251405398086847139926932014947864
    #p = 1897586663842967
    #q = 948793331921483
    return p, q, g

def random_g():
    #p, q = random_pq()
    p, q = pq() 
    g = random.randint(2, p)
    if pow(g, 2, p) == 1:
        #print("1",g)
        return random_g()
    elif pow(g, q, p) == 1:
        #print("2",g)
        return random_g()
    else:
        #print("3",g)
        return g
    
print(random_g())

def random_xy():
    p, q, g = pq()
    x = random.randint(2, p-1)
    #g = random_g()
    y = efektywne_potegowanie(p, x, g)
    return y, x

print(random_xy())

def encryption():
    p, q, g = pq()
    y, x = random_xy()
    
    M = int(input("Wiadomość do zakodowania."))
    #M = 449331
    z = random.randint(2, p-1)
    c1 = efektywne_potegowanie(p, z, g)
    c2 = (M * efektywne_potegowanie(p, z, y)) %p 
    return c1, c2, x

print(encryption())

def decryption():
    
    p, q, g = pq()
    #x = 85720858922740588126983406557358700564488303503847780681244970081981825134000307891191524927525920688713539942945291148501925150988185987835997587278168250875758050589974743606782648062742215240046527
    c1, c2, x = encryption()
    m = (c2 * efektywne_potegowanie(p, p-1-x, c1)) % p
    return m
    
print(decryption())