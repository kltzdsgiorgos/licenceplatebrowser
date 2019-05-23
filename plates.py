import itertools

prefixlist = ['NA', 'NB', 'NE', 'NZ', 'NH', 'NI', 'HM', 'HX']
list2 = ['A', 'B', 'E', 'Z', 'H', 'I', 'K', 'M', 'N', 'O', 'P', 'T', 'Y', 'X']
list3 = [''.join(pair) for pair in itertools.product(prefixlist, list2)]

file = open('platesnew.txt', 'w')

x = 1000
while x < 9000:
	for item in list3:
		y = item + str(x)
		print(y)
		file.write(y)
		file.write('\n')

	x +=1

file.close()