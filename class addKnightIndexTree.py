class TreeNode:
	def __init__(self, pos_i, pos_j):
		self.children = [None]*4
		self.val = [pos_i, pos_j]


def generateKnightIndex(root, row, col):
	# generate the index and call the function recursively
	def getList(root, row,col):

		allPos = list()
		pos_i = root.val[0]
		pos_j = root.val[1]

		allPos.append([pos_i+1, pos_j - 2])
		allPos.append([pos_i + 2, pos_j - 1])
		allPos.append([pos_i + 2, pos_j + 1])
		allPos.append([pos_i + 1, pos_j + 2])

		allPossiblePos = [x for x in allPos if x[0] >= 0 and x[0] <= row and x[1] >= 0 and x[1] <= col]
		return allPossiblePos

	print("[+] Current knight pos: {} possible: {}".format([pos_i, pos_j], getList(row, col, pos_i, pos_j)))
	for x in getList(root, row, col):
		generateKnightIndex(TreeNode(x[0],x[1]), row, col)

root = TreeNode(0,2)
generateKnightIndex(root, 3,3)




