l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
# l = ["1.1.2", "1.3.3", "1.0.12", "1.0.2"]

def answer(l):
	
	obj = [[],[],[]]
	for val in l:
		version = val.split(".")
		for idx, num in enumerate(version):
			obj[idx].append(int(num))
	# print(obj)
	maxX = max(obj[0]) + 1
	maxY = max(obj[1]) + 1
	maxZ = max(obj[2]) + 1

	# initialize the 3d array
	arr3 = [[[0 for k in xrange(maxZ)] for j in xrange(maxY)] for i in xrange(maxX)]
	# initialize the 2d array
	arr2 = [[0 for k in xrange(maxY)] for j in xrange(maxX)]
	# initialize the 1d array
	arr1 = [0 for k in xrange(maxX)]

	for val in l:
		version = val.split(".")
		if len(version) == 3:
			# print int(version[0]), int(version[1]), int(version[2])
			arr3[int(version[0])][int(version[1])][int(version[2])] = 1
		elif len(version) == 2:
			# print int(version[0]), int(version[1])
			arr2[int(version[0])][int(version[1])] = 1
		elif len(version) == 1:
			# print int(version[0])
			arr1[int(version[0])] = 1

	final = []
	for x in range(0, maxX):
		if arr1[x] == 1:
			final.append(str(x))
		for y in range(0, maxY):
			if arr2[x][y] == 1:
				final.append(str(x) + "." + str(y))
			for z in range(0, maxZ):
				if arr3[x][y][z] == 1:
					final.append(str(x) + "." + str(y) + "." + str(z))

	return final

print answer(l)