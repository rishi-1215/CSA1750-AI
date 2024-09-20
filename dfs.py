def dfs(graph, start, visited=None, parent=None, tree=None, order=None):
    if visited is None:
        visited = set()
    if tree is None:
        tree = {}
    if order is None:
        order = []

    visited.add(start)
    order.append(start)
    if parent is not None:
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, start, tree, order)

    return tree, order

def print_tree_with_connections(tree, node, level=0, prefix=""):
    if level == 0:
        print(node)
    else:
        print(prefix + "|-- " + node)

    if node in tree:
        for i, child in enumerate(tree[node]):
            if i == len(tree[node]) - 1:
                extension = "    "
            else:
                extension = "|   "
            print_tree_with_connections(tree, child, level + 1, prefix + extension)

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'H'],
        'F': ['C'],
        'G': ['C'],
        'H': ['E']
    }

    print("DFS starting from vertex 'A':")
    tree, order = dfs(graph, 'A')
    print("\nDFS Traversal Order:")
    print(" -> ".join(order))
    print("\nTree structure with connections:")
    print_tree_with_connections(tree, 'A')
