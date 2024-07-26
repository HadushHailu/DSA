class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        # Helper function to perform DFS and find the max path sum
        def dfs(node):
            if not node:
                return 0, float('-inf')
            
            left_max_single, left_max_top = dfs(node.left)
            right_max_single, right_max_top = dfs(node.right)
            
            max_single = max(left_max_single, right_max_single) + node.val
            max_single = max(max_single, node.val)  # Single node path
            
            max_top = max(left_max_top, right_max_top)
            max_top = max(max_top, left_max_single + node.val + right_max_single)
            
            return max_single, max_top
        
        _, max_sum = dfs(root)
        return max_sum

# Example usage:
# Construct the binary tree
#         1
#        / \
#       2   3
#      / \
#     4   5
#
# Special nodes: 4, 5, 3 (assuming leaf nodes)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

solution = Solution()
print(solution.maxPathSum(root))  # Output: 11 (4 -> 2 -> 1 -> 3)
