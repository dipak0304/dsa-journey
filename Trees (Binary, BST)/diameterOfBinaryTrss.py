class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.diameter = 0  # To keep track of maximum diameter

    # Function to calculate diameter
    def calculate_diameter(self, node):
        if not node:
            return 0
        
        # Recursively find height of left and right subtrees
        left_height = self.calculate_diameter(node.left)
        right_height = self.calculate_diameter(node.right)
        
        # Update diameter at this node
        self.diameter = max(self.diameter, left_height + right_height)
        
        # Return height of tree rooted at this node
        return 1 + max(left_height, right_height)

    def get_diameter(self):
        self.calculate_diameter(self.root)
        return self.diameter


# Example usage
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.left.right.left = Node(6)

print("Diameter of the binary tree:", bt.get_diameter())
