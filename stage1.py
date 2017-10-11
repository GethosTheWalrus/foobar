x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]

x = [14, 27, 1, 4, 2, 50, 3, 1]
y = [2, 4, -1000, 3, 1, 1, 14, 27, 50]

def answer(x, y):
	x = mergesort(x)
	y = mergesort(y)

	if len(x) > len(y):
		loopTarget = x
		compareTo = y
	else:
		loopTarget = y
		compareTo = x

	print loopTarget
	print compareTo

	for idx, val in enumerate(loopTarget):
		if idx == len(loopTarget) - 1:
			return val
		if val != compareTo[idx]:
			return val

	return False

def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break 

	return result

def mergesort(list):
	if len(list) < 2:
		return list

	middle = len(list)/2
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])

	return merge(left, right)

print answer(x, y)