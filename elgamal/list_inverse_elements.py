def list_inverse_elements(num, p):
    for i in range (1, p - 1):
        print(i, num * i % p)

list_inverse_elements(18,23)
