start = 1
end = 100
start_test = 2
prime_nums = []
divisors = 0

for i in range(start,end):
    for j in range(start_test,i):
        if(i % j == 0):
            divisors = divisors + 1
            #print(i, " % ", j , " = ", divisors)
            break
        divisors = 0
    if(divisors == 0):
        prime_nums.append(i)

            

print(prime_nums)


