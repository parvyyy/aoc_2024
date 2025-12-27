import math
from typing import List, Literal
import heapq

type Point = tuple[int, int]
type Direction = Literal['Right', 'Left', 'Down', 'Up', None]

# By using a priority q w/ BFS, we are able to find the
# min cost path. This is similar to Dijkstra's but
# does not have a `dist` array, as we only are focusing
# on `dest`. This is also why we do not have edge relaxation.

def Part1(grid: List[List[str]]):
    n, m = len(grid), len(grid[0])

    def getSourceandDest() -> tuple[Point, Point]:
        src = dest = (0, 0)

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "S":
                    src = (r, c)
                
                if grid[r][c] == "E":
                    dest = (r, c)

        return src, dest

    src, dest = getSourceandDest()

    src_r, src_c = src
    dest_r, dest_c = dest

    # Now, we can consider them as normal tiles.
    grid[src_r][src_c] = "."
    grid[dest_r][dest_c] = "."

    def getNeighbours(r: int, c: int, dirr: Direction):
        def toDir(dr, dc) -> Direction:
            match (dr, dc):
                case 0, 1:
                    return "Right"
                case 0, -1:
                    return "Left"
                case 1, 0:
                    return "Down"
                case -1, 0:
                    return "Up"
                case _:
                    return None
        
        def toOppositeDir(dir: str) -> Direction:
            match (dir):
                case "Left":
                    return "Right"
                case "Right":
                    return "Left"
                case "Up":
                    return "Down"
                case "Down":
                    return "Up"
                case _:
                    return None

        if grid[r][c] == "#":
            return

        neighbours = []
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dr, dc in dirs:
            # Cannot turn 180 degrees.
            if (toDir(dr, dc) == toOppositeDir(dirr)):
                continue

            new_r, new_c = r + dr, c + dc

            if grid[new_r][new_c] == ".":
                neighbours.append((new_r, new_c, toDir(dr, dc)))

        return neighbours

    min_cost = 0

    visited = [[False for _ in range(m)] for _ in range(n)]


    q = [(0, src_r, src_c, None)]
    visited[src_r][src_c] = True
    heapq.heapify(q)

    while q:
        (curr_cost, curr_r, curr_c, curr_dir) = heapq.heappop(q)

        if curr_r == dest_r and curr_c == dest_c:
            min_cost = curr_cost
            break

        for n_r, n_c, n_dir in getNeighbours(curr_r, curr_c, curr_dir):
            if visited[n_r][n_c]:
                continue

            turning_cost = 0 if (n_dir == curr_dir) else 1000
            new_cost = curr_cost + 1 + turning_cost

            visited[n_r][n_c] = True
            heapq.heappush(q, (new_cost, n_r, n_c, n_dir))

    return min_cost

# This must use Dijikstra's to find ALL minium cost paths.
# The exploration space must transform to (r, c, dir) 
# instead of just (r, c). 
def Part2(grid: List[List[str]]):
    n, m = len(grid), len(grid[0])

    def getSourceandDest() -> tuple[Point, Point]:
        src = dest = (0, 0)

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "S":
                    src = (r, c)
                
                if grid[r][c] == "E":
                    dest = (r, c)

        return src, dest

    src, dest = getSourceandDest()

    src_r, src_c = src
    dest_r, dest_c = dest

    # Now, we can consider them as normal tiles.
    grid[src_r][src_c] = "."
    grid[dest_r][dest_c] = "."

    def getNeighbours(r: int, c: int, dirr: Direction):
        def toDir(dr, dc) -> Direction:
            match (dr, dc):
                case 0, 1:
                    return "Right"
                case 0, -1:
                    return "Left"
                case 1, 0:
                    return "Down"
                case -1, 0:
                    return "Up"
                case _:
                    return None
        
        def toOppositeDir(dir: str) -> Direction:
            match (dir):
                case "Left":
                    return "Right"
                case "Right":
                    return "Left"
                case "Up":
                    return "Down"
                case "Down":
                    return "Up"
                case _:
                    return None

        if grid[r][c] == "#":
            return

        neighbours = []
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dr, dc in dirs:
            # Cannot turn 180 degrees.
            if (toDir(dr, dc) == toOppositeDir(dirr)):
                continue

            new_r, new_c = r + dr, c + dc

            if grid[new_r][new_c] == ".":
                neighbours.append((new_r, new_c, toDir(dr, dc)))

        return neighbours

    visited = [[False for _ in range(m)] for _ in range(n)]
    dist = [[math.inf for _ in range(m)] for _ in range(n)]

    q = [(0, src_r, src_c, None)]
    visited[src_r][src_c] = True
    heapq.heapify(q)

    while q:
        (curr_cost, curr_r, curr_c, curr_dir) = heapq.heappop(q)

        if curr_r == dest_r and curr_c == dest_c:
            min_cost = curr_cost
            break

        for n_r, n_c, n_dir in getNeighbours(curr_r, curr_c, curr_dir):
            if visited[n_r][n_c]:
                continue

            turning_cost = 0 if (n_dir == curr_dir) else 1000
            new_cost = curr_cost + 1 + turning_cost

            visited[n_r][n_c] = True
            heapq.heappush(q, (new_cost, n_r, n_c, n_dir))

    return min_cost

with open("small_input.txt", 'r') as fp:
    data = fp.read()
    data = data.split('\n')
    data = [list(d) for d in data]

    # ans1 = Part1(data)
    # print(ans1)

    ans2 = Part2(data)
    print(ans2)



    