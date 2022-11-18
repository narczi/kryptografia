e = 13

while e > 0:
    e = e >> 1
    if(e % 2 == 1):
        print(1)
    elif(e % 2 == 0):
        print(0)


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

print(dec2bin(13))
