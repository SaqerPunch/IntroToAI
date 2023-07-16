import random
from collections import deque
 
def generate_gridworld(size, block_chance):
    gridworld = [[False for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if random.random() < block_chance:
                gridworld[i][j] = True
    return gridworld
 
def is_path_exist_astar(gridworld):
    rows, cols = len(gridworld), len(gridworld[0])
    start = (0, 0)
    goal = (rows - 1, cols - 1)
 
    g_score = {start: 0}
    f_score = {start: 0}
    queue = deque([start])
 
    while queue:
        current = queue.popleft()
        if current == goal:
            return True
 
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and not gridworld[nr][nc]:
                new_g_score = g_score[current] + 1
 
                if (nr, nc) not in g_score:
                    g_score[nr, nc] = new_g_score
                    f_score[nr, nc] = new_g_score + abs(nr - goal[0]) + abs(nc - goal[1])
                    queue.append((nr, nc))
                else:
                    if new_g_score < g_score[nr, nc]:
                        g_score[nr, nc] = new_g_score
                        f_score[nr, nc] = new_g_score + abs(nr - goal[0]) + abs(nc - goal[1])
                        queue.append((nr, nc))
 
    return False
 
# Generate 50 gridworlds
num_gridworlds = 50
gridworlds = []
for _ in range(num_gridworlds):
    grid = generate_gridworld(101, 0.3)
    while not is_path_exist_astar(grid):
        grid = generate_gridworld(101, 0.3)
    gridworlds.append(grid)
