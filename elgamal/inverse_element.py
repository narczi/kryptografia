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


print(element_odwrotny(18,23))
