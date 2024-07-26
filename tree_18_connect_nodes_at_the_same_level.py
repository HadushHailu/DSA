class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None

# Function to connect nodes at the same level
def connectNodes(root):
    if not root:
        return

    # Initialize a queue for level order traversal
    queue = []
    queue.append(root)

    # While there are nodes in the queue
    while queue:
        # Number of nodes at current level
        size = len(queue)

        # Previous node at current level
        prev = None

        # Process all nodes at current level
        for i in range(size):
            # Dequeue the front node from the queue
            node = queue.pop(0)

            # If there is a previous node at this level, set its nextRight to current node
            if prev:
                prev.nextRight = node

            # The current node becomes the previous node for the next iteration
            prev = node

            # Enqueue the left and right children of the current node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Mark the end of the current level
        prev.nextRight = None

# Function to print level order traversal using nextRight pointers
def printLevelOrderUsingNextRight(root):
    while root:
        current = root
        while current:
            print(current.data, end=" ")
            current = current.nextRight
        print()
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            temp = root
            while temp and not (temp.left or temp.right):
                temp = temp.nextRight
            if not temp:
                root = None
            elif temp.left:
                root = temp.left
            else:
                root = temp.right

# Function to print inorder traversal
def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data, end=" ")
        printInOrder(root.right)

# Driver code
if __name__ == "__main__":
    # Create the binary tree
    root = Node(10)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(1)
    root.right.right = Node(2)

    # Connect nodes at the same level
    connectNodes(root)

    # Print level order traversal using nextRight pointers
    print("Level order traversal using nextRight pointers:")
    printLevelOrderUsingNextRight(root)

    # Print inorder traversal
    print("\nInorder traversal:")
    printInOrder(root)
