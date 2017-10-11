import fractions

# m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# m = [[1]]
# m = [[1, 2, 3, 0, 0, 0], [4, 5, 6, 0, 0, 0], [7, 8, 9, 1, 0, 0], [0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# m = [
#         [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
#         [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
#         [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
#         [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
#         [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]
def answer(m):

	if len(m) == 1:
		return [1, 1]

	R = []
	Q = []
	I = []
	O = []
	F = []
	#identify absorbing states and the order that the states
	#will be in when translated into standard form
	absorbing = []
	transition = []
	absorbingStates = []
	transitionStates = []
	for stateNum, state in enumerate(m):
		if sum(state) == 0:
			absorbing.append(state)
			absorbingStates.append(stateNum)
		else:
			transition.append(state)
			transitionStates.append(stateNum)

	order = absorbingStates + transitionStates

	#reorder each transition state's values according to the 
	#state order and change numbers to probabilities
	for stateNum, state in enumerate(transition):
		tmpState = state[:]
		for valNum, val in enumerate(state):
			tmpState[valNum] = float(state[order[valNum]]) / float(sum(state))
		transition[stateNum] = tmpState[:]
		#get matrix R
		RIndex = []
		for i in range(0, len(absorbing)):
			RIndex.append(transition[stateNum][i])
		R.append(RIndex)
		#get matrix Q
		QIndex = []
		for i in range(len(absorbing), len(m)):
			QIndex.append(transition[stateNum][i])
		Q.append(QIndex)

	#add a 1 to each absorbing state to make it an identity
	#matrix
	for stateNum, state in enumerate(absorbing):
		state[stateNum] = 1

	#concatenate the lists so that the absorbing states
	#come before the transition states
	standard = absorbing + transition

	#find F matrix
	ICount = 0;
	for rowIdx, row in enumerate(Q):
		IIndex = []
		for valIdx, val in enumerate(row):
			if rowIdx == ICount and valIdx == ICount:
				IIndex.append(1)
			else:
				IIndex.append(0)
		I.append(IIndex)
		ICount += 1
	F = getMatrixInverse(subtractMatrices(I, Q))

	FR = multiplyMatrices(F, R)

	# generate numerators
	numerators = []
	for i in FR[0]:
		numerator = fractions.Fraction(i).limit_denominator().numerator
		numerators.append(numerator)

	# generate denominators
	denominators = []
	for i in FR[0]:
		denominator = fractions.Fraction(i).limit_denominator().denominator
		denominators.append(denominator)

	lcd = 1
	for val in denominators:
		lcd = getLcm(lcd, val)
	# print lcd
	for idx, num in enumerate(numerators):
		numerators[idx] = num * (lcd / denominators[idx])

	# numerators[:] = (value for value in numerators if value != 0)
	final = []
	for idx, val in enumerate(absorbing):
		final.append(numerators[idx])
	final.append(lcd)

	# print reducefract(Fraction(FR[0][1]).numerator, Fraction(FR[0][1]).denominator)

	# for row in FR:
	# 	for val in row:
	# 		print val.as_integer_ratio()
	# print numerators
	# print denominators
	# for row in FR:
	# 	print row

	return final

def reducefract(n, d):
    '''Reduces fractions. n is the numerator and d the denominator.'''
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    assert d!=0, "integer division by zero"
    assert isinstance(d, int), "must be int"
    assert isinstance(n, int), "must be int"
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return n, d

def multiplyMatrices(a, b):
	if len(a[0]) > len(b[0]):
		rowNum = len(a[0])
	else:
		rowNum = len(b[0])

	if len(a) > len(b):
		colNum = len(a)
	else:
		colNum = len(b)

	output = [[0 for k in xrange(rowNum)] for j in xrange(colNum)]
	# iterate through rows of a
	for i in range(len(a)):
	   # iterate through columns of b
	   for j in range(len(b[0])):
	       # iterate through rows of b
	       for k in range(len(b)):
	           output[i][j] += a[i][k] * b[k][j]
	return output

def subtractMatrices(a, b):
	output = []
	for rowIdx, row in enumerate(a):
		outputRow = []
		for valIdx, val in enumerate(row):
			outputRow.append(val - b[rowIdx][valIdx])
		output.append(outputRow)
	return output

def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def getLcm(x, y):
	"""This function takes two
	integers and returns the L.C.M."""

	if x == 0:
		return y

		if y == 0:
			return x

	# choose the greater number
	if x > y:
		greater = x
	else:
		greater = y

	while(True):
		if((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater += 1

	return lcm

print answer(m)