# Binary Search 
def binarySearch(inorder, l, r, d):
	print("inorder: {0} l: {1} r: {2} d:{3}".format(inorder, l, r, d))
	mid = (l + r) >> 1
	if (inorder[mid] == d): 
		return mid 
	elif (inorder[mid] > d): 
		return binarySearch(inorder, l, 
							mid - 1, d) 
	else: 
		return binarySearch(inorder, 
							mid + 1, r, d) 

# Function to print Leaf Nodes by doing 
# preorder traversal of tree using 
# preorder and inorder arrays. 
def leafNodesRec(preorder, inorder, 
					l, r, ind, n):
	print("preorder: {0} inorder: {1} l: {2} r: {3} ind: {4} n:{5}".format(preorder, inorder, l, r, ind, n))
	# If l == r, therefore no right or left subtree. 
	# So, it must be leaf Node, print it. 
	if(l == r): 
		print(inorder[l], end = " ") 
		ind[0] = ind[0] + 1
		print("IND-l==r: {}".format(ind))
		return

	# If array is out of bound, return. 
	if (l < 0 or l > r or r >= n): 
		return

	# Finding the index of preorder element 
	# in inorder array using binary search. 
	loc = binarySearch(inorder, l, r, 
					preorder[ind[0]]) 
	print("LOC: {}".format(loc))

	# Incrementing the index. 
	ind[0] = ind[0] + 1
	print("IND-L: {}".format(ind))

	# Finding on the left subtree. 
	leafNodesRec(preorder, inorder,	 
				l, loc - 1, ind, n) 

	print("IND-R: {}".format(ind))
	# Finding on the right subtree. 
	leafNodesRec(preorder, inorder, 
				loc + 1, r, ind, n) 

# Finds leaf nodes from 
# given preorder traversal. 
def leafNodes(preorder, n): 

	# To store inorder traversal 
	inorder = [0] * n 
	
	# Copy the preorder into another array. 
	for i in range(n): 
		inorder[i] = preorder[i] 

	# Finding the inorder by sorting the array. 
	inorder.sort() 
	
	# Point to the index in preorder. 
	ind = [0] 
	
	# Print the Leaf Nodes. 
	leafNodesRec(preorder, inorder, 0, 
				n - 1, ind, n) 


# Driver Code 
preorder = [890, 325, 290, 530, 965] 
n = len(preorder) 
leafNodes(preorder, n) 

# This code is contributed 
# by SHUBHAMSINGH10 
