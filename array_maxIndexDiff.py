def maxIndexDiffOn2(a, n):
	maxDiff = 0

	for i in range(n):
		tmpMaxIndexDiff = 0
		for j in range(i,n):
			if a[i] <= a[j]:
				tmpMaxIndexDiff = j-i
		if tmpMaxIndexDiff > maxDiff:
			maxDiff = tmpMaxIndexDiff
	return maxDiff


def maxIndexDiffon(a, n): 
        ##Your code here
        if n <= 1:
            return 0

        # Create LMin and RMax arrays
        LMin = [0] * n
        RMax = [0] * n
    
        # Construct LMin[] array
        LMin[0] = a[0]
        for i in range(1, n):
            LMin[i] = min(a[i], LMin[i - 1])
        print("LMin: {}".format(LMin))
    
        # Construct RMax[] array
        RMax[n - 1] = a[n - 1]
        for j in range(n-2, -1, -1):
            RMax[j] = max(a[j], RMax[j + 1])
        print("RMax: {}".format(RMax))

        # Traverse LMin and RMax to find the maximum j - i
        i, j = 0, 0
        maxDiff = 0
        while j < n and i < n:
        	print("maxDiff: {} i: {} j: {}".format(maxDiff, i, j))
        	if LMin[i] <= RMax[j]:
        		maxDiff = max(maxDiff, j - i)
        		j += 1
        	else:
        		i += 1
    
        return maxDiff

n = 9
a = [34, 8, 10, 3, 2, 80, 30, 33, 1]

# n = 2
# a = [1, 10]
print(maxIndexDiffon(a,n))


