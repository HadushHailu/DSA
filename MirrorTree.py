class Node:
	def __init__(self, data = None):
		self.val = data
		self.right = None
		self.left = None


def inser(root,data):
	root = insertNode(root, data)

def insertNode(root, data):
	node = Node(data)
	if root is None:
		return Node(data)

	else:
		if data > root.val:
			root.right = insertNode(root.right, data)
		else:
			root.left = insertNode(root.left, data)

		return root

def dfs(root):
	if root is None:
		pass
	else:
		dfs(root.left)
		print("[+] {}".format(root.val))
		dfs(root.right)

def mirror(root):
	print(root.right.val)
	tmpNode = root.left
	root.left = root.right
	root.right = tmpNode

	if root is not None:
		mirror(root.left)
		#mirror(root.right)

if __name__ == "__main__":
	root = Node(10)
	inser(root, 4)
	inser(root, 1)
	inser(root, 9)
	inser(root, 15)
	inser(root, 13)
	#dfs(root)
	

	#mirror(root)
	tmpNode = root.left
	root.left = root.right
	root.right = tmpNode
	dfs(root)


