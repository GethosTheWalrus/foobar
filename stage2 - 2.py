def answer(x, y):
	num = getBase(y)
	
	jump = y + 1
	for i in range(0, x - 1):
		num += jump
		jump += 1

	return num

def getBase(y):
	tmp = y
	for i in range(1, y):
		tmp += i - 1

	return tmp

def getBaseRecursive(y):
	if y == 1:
		return 1
	else:
		return getBase(y - 1) + y - 1

print answer(1000000, 1000000)