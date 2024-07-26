class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.isEndOfWord = False

class UniqueRow:
	def insert(self, root, keyList):
		node = root
		unique_row = []
		counter = 0

		for char in keyList:
			index = char

			unique_row.append(char)

			if node.children[index] is None:
				counter += 1
				print("[+] adding {0} counter: {1}".format(char, counter))
				node.children[index] = TrieNode()

			node = node.children[index]

		node.isEndOfWord = True

		print("[-] counter is: {}".format(counter)) 
		if counter == 0:
			unique_row = []

		return unique_row


if __name__ == "__main__":
	this_node = UniqueRow()
	root = TrieNode()

	matrix = [[1,1,0,1], [1,0,0,1], [1,1,0,1]]
	unique_row_list = []
	for l in matrix:
		ret = this_node.insert(root, l)
		if len(ret):
			unique_row_list.append(ret)
	print(unique_row_list)



