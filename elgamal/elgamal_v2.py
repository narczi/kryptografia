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
        

def reszta_kwadratowa(prime, num):
    result = bin_exp(num, int((prime-1)/2), prime)
    if result == prime-1:
        return 0
    if result == 1:
        return 1

def losuj(podloga, sufit):
    liczba = podloga
    while(liczba < podloga + 1):
        liczba = secrets.randbelow(sufit) 

    return liczba

def is_prime(num, tests):
    for i in range(1, tests + 1):
        pierwszosc_num = test_fermata(num)
        if(pierwszosc_num == False):
            break
    return pierwszosc_num

def generate_prime(tests, bity):
    pierwszosc_q = False
    while(pierwszosc_q == False):
        q = random.getrandbits(bity) 
        pierwszosc_q = is_prime(q, tests)
    return q
    
def pq(tests):
    bity = 1000
    q = generate_prime(tests,bity)
    p = 2 * q + 1
    while(is_prime(q, tests) != True or is_prime(p, tests) != True):
        q = generate_prime(tests,bity)
        p = 2 * q + 1
        if(is_prime(p, tests) == True):
            return p, q
        else:
            continue

def pq_preset(tests):
    q = 10364539713338475201245149609093379930613330371908584546926234157497879858026895663465498007748097008368932515854892195916533872835556288868871760271733703492959128313121624455357676017367979852459493487449003258519699920583185854713356355758902832122836711218144979612465474268935081505875258299091301
    p = 20729079426676950402490299218186759861226660743817169093852468314995759716053791326930996015496194016737865031709784391833067745671112577737743520543467406985918256626243248910715352034735959704918986974898006517039399841166371709426712711517805664245673422436289959224930948537870163011750516598182603

    q = 3742315748166351629852492510410534388607165608583012935998444750334803288232308358326901812244803352041570578435731492335911766119150279606859650657954085083834668429849485735078997042607326361140379805509738761160864112323902921224858799383004574862013948259134155331761989010799641715117924015557799
    p = 7484631496332703259704985020821068777214331217166025871996889500669606576464616716653803624489606704083141156871462984671823532238300559213719301315908170167669336859698971470157994085214652722280759611019477522321728224647805842449717598766009149724027896518268310663523978021599283430235848031115599

    q = 3026092757207133828182171682114492891460242807317728722405756676542049470335926269483098113976840733042965553412177273824376413054042327206983600522350966092903743738566644025523720341172045277009868307584012907324640219806116880203890602887875736172578642658265213262258881643918528776091446419297253
    p = 6052185514414267656364343364228985782920485614635457444811513353084098940671852538966196227953681466085931106824354547648752826108084654413967201044701932185807487477133288051047440682344090554019736615168025814649280439612233760407781205775751472345157285316530426524517763287837057552182892838594507

    q = 2763938369133367270982315607842815251369385134514017988736447728335086162374069017921820309236090678089902076705298718366277160403478337744679766983826885640446925416982372707600954602007922317761997635934085226683690696639897917135027747502889881411553282988489770427719744128712010176544735757207893
    p = 5527876738266734541964631215685630502738770269028035977472895456670172324748138035843640618472181356179804153410597436732554320806956675489359533967653771280893850833964745415201909204015844635523995271868170453367381393279795834270055495005779762823106565976979540855439488257424020353089471514415787
    return p, q


def generate_keys():
    p, q = pq_preset(30)

    g = losuj(1,p)
    g_2 = bin_exp(g,2,p)
    g_q = bin_exp(g,q,p)

    while(NWD(p,g) != 1 and (g_2 == 1 or g_q == 1)):
        g = losuj(1,p)
        g_2 = bin_exp(g,2,p)
        g_q = bin_exp(g,q,p)
        
    x = losuj(1,p-1)

    y = bin_exp(g,x,p)

    print("p = ", p, "\nq = ", q, "\ng = ", g, "\ny = ", y, "\nx = ", x)


    return {'p': p, 
            'g': g,
            'y': y,
            'x': x}

def pg():
    p = 120471683029418687071538440325434591814539544830974289094629223908748885878701977499366767041636724573600462526018305751410401637006900776611105633028708553943579675496053770805388766680786652129988323
    g = 49715514348199090400843794814660308877056073622245224797010955964356803526998184663309372595341717728544108806549188510677381031650589317444134306192256169850270129536251405398086847139926932014947864
    return p, g

def encrypt(publickey, M):
    #p, g = pg()
    p = publickey["p"]
    g = publickey["g"]
    y = publickey["y"]

    z = losuj(1,p-1)

    c_1 = bin_exp(g,z,p)
    c_2_half = bin_exp(y,z,p)

    c_2 = (c_2_half * M) % p

    print("M = ", M)
    print("z = ", z)
    print("c_1 = ", c_1)
    print("c_2_half = ", c_2_half)
    print("c_2 = ", c_2)

    return {'c_1': c_1, 
            'c_2': c_2}


def decrypt(privatekey, szyfrogram):
    p = privatekey["p"]
    x = privatekey["x"]

    c_1 = szyfrogram["c_1"]
    c_2 = szyfrogram["c_2"]

    c_1_inv = element_odwrotny(c_1, p)
    c_1_pow = bin_exp(c_1_inv,x,p)
    M_decrypt = (c_2 * c_1_pow) % p
    return M_decrypt

def main():

    key_pair = generate_keys()

    public_key = {}
    private_key = {}

    public_key['p'] = key_pair['p']
    public_key['g'] = key_pair['g']
    public_key['y'] = key_pair['y']

    private_key['p'] = key_pair['p']
    private_key['x'] = key_pair['x']


    message = 421807
    szyfrogram = encrypt(public_key, message)

    print("M_decrypt = ", decrypt(private_key, szyfrogram))

if __name__ == "__main__":
    main()