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


def phi(n):
    numbers = []
    for a in range(1,n):
        if(NWD(a,n) == 1):
            numbers.append(a)
            
    return numbers


def inverse_elements_list(totients, n):
    ie_list = []
    for tot in totients:
        for num in totients:
            if(tot * num % n == 1):
                ie_list.append(num)

    return ie_list

def inv_elem(totients, n, a):
    a_inv = 0
    for tot in totients:
        for num in totients:
            if(tot * num % n == 1):
                if(tot == a):
                    a_inv = num

    return a_inv

def GCD_modulo_extended(a,b):
    x = 1
    y = 0
    remainder = 0
    s = 1

    while(b != 0):
        c = a % b
        quotient = a // b
        a = b
        b = c

        remainder_prim = remainder
        s_prim = s
        remainder = x - quotient * remainder
        s = y - quotient * s
        x = remainder_prim
        y = s_prim

    return (a, x, y)


def main():
    a = 47
    n = 240
    totients = phi(n)
    inv_totients = inverse_elements_list(totients, n)
    a_inv = inv_elem(totients, n, a)
    gcd_E = GCD_modulo_extended(a, n)

    print(f"Totients phi({n}):\n {totients}\n")
    print(f"Elementy odwrotne:\n {inv_totients}\n")
    print(f"Element odwrotny do {a} to {a_inv}\n")
    print(f"GCD_modulo_extended:\n {gcd_E}\n")
    print(f"{a} * {a_inv} mod {n} = {(a*a_inv) % n}")

if __name__ == "__main__":
    main()


