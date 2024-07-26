def sampleBacktrack(L,index):
	for i in range(index, len(L)):
		print("Current i: {}".format(L[i]))
		sampleBacktrack(L, index+1)

index = 0
L = [1,2,3]
sampleBacktrack(L,index)
