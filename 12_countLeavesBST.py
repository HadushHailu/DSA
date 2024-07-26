class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        if root is None:
            return
        
        # Recursively convert the left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
    def countLeaves(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1
        else:
            return self.countLeaves(root.left) + self.countLeaves(root.right)

    def insert(self, root,data):
        root = self.insertNode(root, data)

    def insertNode(self, root, data):
        node = Node(data)
        if root is None:
            return Node(data)

        else:
            if data > root.data:
                root.right = self.insertNode(root.right, data)
            else:
                root.left = self.insertNode(root.left, data)

            return root

if __name__ == "__main__":
    sol = Solution()
    root = Node(10)
    sol.insert(root, 1)
    sol.insert(root, 4)
    sol.insert(root, 7)
    sol.insert(root, 9)
    sol.insert(root, 15)
    sol.insert(root, 13)
    sol.insert(root, 6)

    print(sol.countLeaves(root))






