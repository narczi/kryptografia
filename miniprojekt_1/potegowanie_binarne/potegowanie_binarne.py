def dec2bin(decimal):
    retval = []
    while(decimal > 0):
        if(decimal % 2 == 0):
            retval.append(0)
        elif(decimal % 2 == 1):
            retval.append(1)

        decimal = decimal // 2

    retval.reverse()
    return retval

#el to liczba bitów liczby k w zapisie dwojkowym

b = 4
e = 13
m = 497

def bin_exp(b,e,m):
    y = 1
    i = 0

    e_binary = dec2bin(e)
    e_bits = len(e_binary)

    while i < e_bits:
        if(e_binary[i] == 1):
            y = (y * b) % m
        y = (y * y) % m

        i = i + 1

    return y

print(bin_exp(b,e,m))
