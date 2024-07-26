def generateKnightIndex(row, col, pos_i, pos_j):
	# generate the index and call the function recursively
	def getList(row,col,pos_i, pos_j):

		allPos = list()
		allPos.append([pos_i+1, pos_j - 2])
		allPos.append([pos_i + 2, pos_j - 1])
		allPos.append([pos_i + 2, pos_j + 1])
		allPos.append([pos_i + 1, pos_j + 2])

		allPossiblePos = [x for x in allPos if x[0] >= 0 and x[0] <= row and x[1] >= 0 and x[1] <= col]
		return allPossiblePos

	print("[+] Current knight pos: {} possible: {}".format([pos_i, pos_j], getList(row, col, pos_i, pos_j)))
	for x in getList(row, col, pos_i, pos_j):
		generateKnightIndex(row, col,x[0], x[1])


generateKnightIndex(3,3,0,2)






