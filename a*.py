
import heapq
class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic
    def __lt__(self, other):
        return self.total_cost < other.total_cost
def astar_search(start, goal, heuristic_func, neighbors_func):
    open_set = []
    closed_set = set()
    start_node = Node(state=start, cost=0, heuristic=heuristic_func(start))
    heapq.heappush(open_set, start_node)
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            path.reverse()
            return path
        closed_set.add(current_node.state)
        for neighbor in neighbors_func(current_node.state):
            if neighbor in closed_set:
                continue
            tentative_cost = current_node.cost + 1
            neighbor_node = Node(state=neighbor, parent=current_node, cost=tentative_cost, heuristic=heuristic_func(neighbor))
            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)
            else:
                for node in open_set:
                    if node.state == neighbor and node.total_cost > neighbor_node.total_cost:
                        open_set.remove(node)
                        heapq.heappush(open_set, neighbor_node)
    return None  
def heuristic(state):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
def neighbors(state):
    x, y = state
    possible_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(x, y) for x, y in possible_neighbors if 0 <= x < 10 and 0 <= y < 10]
start = (0, 0)
goal = (9, 9)
path = astar_search(start, goal, heuristic, neighbors)
if path:
    print("Path found:", path)
else:
    print("No path found")
