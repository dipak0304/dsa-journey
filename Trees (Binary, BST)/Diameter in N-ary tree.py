class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

class NaryTree:
    def __init__(self, root_key):
        self.root = Node(root_key)
        self.diameter = 0

    # Recursive function to find height and update diameter
    def _height(self, node):
        if not node:
            return 0
        
        # Store the heights of all children
        heights = []
        for child in node.children:
            heights.append(self._height(child))
        
        # If node has no children
        if not heights:
            return 1
        
        # Sort heights descending to get two largest heights
        heights.sort(reverse=True)
        
        # If there are at least two children, update diameter
        if len(heights) >= 2:
            self.diameter = max(self.diameter, heights[0] + heights[1])
        else:
            self.diameter = max(self.diameter, heights[0])
        
        # Return height of this node
        return 1 + max(heights)

    def get_diameter(self):
        self._height(self.root)
        return self.diameter


# Example usage
tree = NaryTree("A")
tree.root.children = [Node("B"), Node("C"), Node("D")]
tree.root.children[0].children = [Node("E"), Node("F")]
tree.root.children[2].children = [Node("G")]

print("Diameter of the N-ary tree:", tree.get_diameter())
