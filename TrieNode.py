class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def insert(self, root, key):
        node = root
        for char in key:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True

    def search(self, root, key):
        node = root
        for char in key:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.isEndOfWord

    def deleteKey(self, root, key, depth=0):
        if root is None:
            return None

        # If we have reached the end of the key
        if depth == len(key):
            if root.isEndOfWord:
                root.isEndOfWord = False

            # If the node has no children, we can delete it
            if all(child is None for child in root.children):
                return None

            return root

        index = ord(key[depth]) - ord('a')
        root.children[index] = self.deleteKey(root.children[index], key, depth + 1)

        # If the root has no children and it is not the end of another word
        if not root.isEndOfWord and all(child is None for child in root.children):
            return None

        return root

# Example usage
root = TrieNode()
trie = Trie()
trie.insert(root, "hello")
trie.insert(root, "hell")
trie.insert(root, "heaven")

print(trie.search(root, "hello"))  # Output: True
print(trie.search(root, "hell"))   # Output: True
print(trie.search(root, "heaven")) # Output: True

trie.deleteKey(root, "hell")
print(trie.search(root, "hell"))   # Output: False
print(trie.search(root, "hello"))  # Output: True
print(trie.search(root, "heaven")) # Output: True

trie.deleteKey(root, "heaven")
print(trie.search(root, "heaven")) # Output: False
