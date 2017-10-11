def answer(n):
	num = int(n)
	steps = 0
	while num > 1:
		if num % 2 == 0:
			num = num / 2
		else:
			if ((num - 1) / 2) % 2 == 0 or (num - 1) == 2:
				num = num - 1
			else:
				num = num + 1

		steps += 1

	return steps

# print answer(16)