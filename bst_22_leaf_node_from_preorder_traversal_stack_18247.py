# Stack based Python program to print 
# leaf nodes from preorder traversal. 

# Print the leaf node from the given 
# preorder of BST. 
def leafNode(preorder, n): 
	s = [] 
	i = 0
	for j in range(1, n): 
		found = False
		if preorder[i] > preorder[j]: 
			s.append(preorder[i])
			print("append to s: {}".format(s)) 

		else: 
			while len(s) != 0:
				print("prorder[j]:{} s[-1]:{}".format(preorder[j], s[-1]))
				if preorder[j] > s[-1]: 
					s.pop(-1) 
					print("popped from s: {}".format(s)) 
					found = True
				else: 
					break

		if found: 
			print(preorder[i]) 
		i += 1

	# Since rightmost element is 
	# always leaf node. 
	print("stack: {}".format(s))
	print(preorder[n - 1]) 

# Driver code 
if __name__ == '__main__': 
	preorder = [100,50,20,40] 
	n = len(preorder) 

	leafNode(preorder, n) 

# This code is contributed by PranchalK 
