class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def bfs(root):
    from collections import deque
    queue = deque([root])
    levels = {}  # To store nodes level by level
    bfs_order = []  # To store the BFS traversal order

    level = 0
    while queue:
        levels[level] = []
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()
            bfs_order.append(node.value)  # Add to BFS traversal order
            levels[level].append(node.value)
            for child in node.children:
                queue.append(child)

        level += 1

    return levels, bfs_order

# Function to print the tree levels
def print_tree_levels(levels):
    for level in levels:
        print(f"Level {level}: {' -> '.join(map(str, levels[level]))}")

# Example Usage
if __name__ == "__main__":
    # Create tree nodes
    root = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')
    nodeG = TreeNode('G')
    
    # Build the tree
    root.add_child(nodeB)
    root.add_child(nodeC)
    nodeB.add_child(nodeD)
    nodeB.add_child(nodeE)
    nodeC.add_child(nodeF)
    nodeC.add_child(nodeG)
    
    # Perform BFS and get the tree levels and traversal order
    levels, bfs_order = bfs(root)
    
    # Print the tree levels
    print_tree_levels(levels)
    
    # Print the BFS traversal order
    print("BFS Traversal Order:", ' -> '.join(bfs_order))
