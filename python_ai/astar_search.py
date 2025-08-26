import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def astar(start, goal, grid):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        for next_pos in get_neighbors(current_node.position, grid):
            if next_pos in closed_set:
                continue
            neighbor = Node(next_pos, current_node)
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h
            if not any(open_node.position == neighbor.position and open_node.f <= neighbor.f for open_node in open_list):
                heapq.heappush(open_list, neighbor)
    return None

def get_neighbors(pos, grid):
    x, y = pos
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

if __name__ == "__main__":
    grid = [[0,0,0,0],[1,1,0,1],[0,0,0,0],[0,1,1,0]]
    start = (0,0)
    goal = (3,3)
    path = astar(start, goal, grid)
    print("Path:", path)
