class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.max_sum = float('-inf')  # Track maximum sum globally

    # Recursive helper function
    def _max_path_sum(self, node):
        if not node:
            return 0
        
        # Maximum sum on left and right subtrees (ignore negative sums)
        left = max(self._max_path_sum(node.left), 0)
        right = max(self._max_path_sum(node.right), 0)
        
        # Update max_sum if path through this node is larger
        self.max_sum = max(self.max_sum, node.key + left + right)
        
        # Return max sum path starting from this node
        return node.key + max(left, right)

    def get_max_sum_path(self):
        self._max_path_sum(self.root)
        return self.max_sum


# Example usage
bt = BinaryTree()
bt.root = Node(10)
bt.root.left = Node(2)
bt.root.right = Node(10)
bt.root.left.left = Node(20)
bt.root.left.right = Node(1)
bt.root.right.right = Node(-25)
bt.root.right.right.left = Node(3)
bt.root.right.right.right = Node(4)

print("Maximum sum path between any two nodes:", bt.get_max_sum_path())
