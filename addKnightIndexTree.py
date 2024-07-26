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

	listPossible = getList(root, row, col)
	print("[+] Current knight pos: {} possible: {}".format([root.val[0], root.val[1]], listPossible))

	if len(listPossible):
		counter = 0
		for x in getList(root, row, col):
			root.children[counter] = TreeNode(x[0],x[1])
			generateKnightIndex(root.children[counter], row, col)
			counter += 1


def dfs(root):
	if any(root.children):
		print("Current Node: {} len child: {}".format([root.val[0], root.val[1]], len([x for x in root.children if x is not None])))
		for i in range(len([x for x in root.children if x is not None])):
			#print("Current Node: {} len child: {}".format([root.val[0], root.val[1]], len([x for x in root.children if x is not None])))
			dfs(root.children[i])

def dfsDfs(root, holder, counter, posX, posY):
	if any(root.children):
		counter += 1
		print("Current Node: {} len child: {} holder: {} counter: {}".format([root.val[0], root.val[1]], len([x for x in root.children if x is not None]), holder, counter))
		for i in range(len([x for x in root.children if x is not None])):
			dfsDfs(root.children[i], holder, counter, posX, posY)

	if root.val[0] == posX and root.val[1] == posY:
		holder.append(counter)
	print("Current Node: {} len child: {} holder: {} counter: {}".format([root.val[0], root.val[1]], len([x for x in root.children if x is not None]), holder, counter))




root = TreeNode(0,3)
generateKnightIndex(root, 6,6)

dfs(root)

holder = []
dfsDfs(root, holder, 0, 6,2)
print("holder: {} min: {}".format(holder, min(holder)))



