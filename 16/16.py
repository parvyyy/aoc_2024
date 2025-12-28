import math
from typing import List, Literal
import heapq

type Point = tuple[int, int]
type Direction = Literal['Right', 'Left', 'Down', 'Up', None]
class Direction:
    @staticmethod
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
            
    @staticmethod
    def toOpposite(dir: str) -> Direction:
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
            
    @staticmethod
    def toIdx(dir: str) -> int:
        match (dir):
            case "Left":
                return 3
            case "Right":
                return 1
            case "Up":
                return 0
            case "Down":
                return 2
            case _:
                return None


# By using a priority q w/ BFS, we are able to find the
# min cost path. This is similar to Dijkstra's but
# does not have a `dist` array, as we only are focusing
# on `dest`. This is also why we do not have edge relaxation.

def Part1(grid: List[List[str]], src: Point, dest: Point):
    n, m = len(grid), len(grid[0])

    src_r, src_c = src
    dest_r, dest_c = dest

    def getNeighbours(r: int, c: int, dirr: Direction) -> list:
        if grid[r][c] == "#":
            return []

        neighbours = []
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dr, dc in dirs:
            # Cannot turn 180 degrees.
            if (Direction.toDir(dr, dc) == Direction.toOpposite(dirr)):
                continue

            new_r, new_c = r + dr, c + dc

            if grid[new_r][new_c] == ".":
                neighbours.append((new_r, new_c, Direction.toDir(dr, dc)))

        return neighbours

    min_cost = 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    q = [(0, src_r, src_c, None)]
    heapq.heapify(q)

    visited[src_r][src_c] = True

    while q:
        (curr_cost, curr_r, curr_c, curr_dir) = heapq.heappop(q)

        # The `min-heap`'s heuristic in minimising the cost
        # coupled with the cost only increasing ensures that
        # arriving at `dst` for the first time is most optimal.
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


def Part2(grid: List[List[str]], src: Point, dest: Point, min_cost: int):
    n, m = len(grid), len(grid[0])

    src_r, src_c = src
    dest_r, dest_c = dest

    def getNeighbours(r: int, c: int, dirr: Direction) -> list:
        if grid[r][c] == "#":
            return []

        neighbours = []
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for dr, dc in dirs:
            # Cannot turn 180 degrees.
            if (Direction.toDir(dr, dc) == Direction.toOpposite(dirr)):
                continue

            new_r, new_c = r + dr, c + dc

            if grid[new_r][new_c] == ".":
                neighbours.append((new_r, new_c, Direction.toDir(dr, dc)))

        return neighbours

    # Must allow exploration from all directions to each cell, to find
    # the true `min` per cell r, c.
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    distA = [[math.inf for _ in range(m)] for _ in range(n)]

    q = [(0, src_r, src_c, None)]
    heapq.heapify(q)

    # Set the cell visited from all directions
    for d in range(4):
        visited[src_r][src_c][d] = True

    distA[src_r][src_c] = 0

    while q:
        (curr_cost, curr_r, curr_c, curr_dir) = heapq.heappop(q)

        for n_r, n_c, n_dir in getNeighbours(curr_r, curr_c, curr_dir):
            n_dir = Direction.toIdx(n_dir)

            if visited[n_r][n_c][n_dir]:
                continue

            turning_cost = 0 if (n_dir == curr_dir) else 1000
            new_cost = curr_cost + 1 + turning_cost

            visited[n_r][n_c][n_dir] = True

            # Update `dist` if exploration will yield a lower cost to
            # the neighbour tile.
            distA[n_r][n_c] = min(distA[n_r][n_c], new_cost)

            heapq.heappush(q, (new_cost, n_r, n_c, n_dir))
    

    # Repeat this process, instead going from dest -> src
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    distB = [[math.inf for _ in range(m)] for _ in range(n)]

    q = [(0, dest_r, dest_c, None)]
    heapq.heapify(q)

    # Set the cell visited from all directions
    for d in range(4):
        visited[dest_r][dest_c][d] = True

    distB[dest_r][dest_c] = 0

    while q:
        (curr_cost, curr_r, curr_c, curr_dir) = heapq.heappop(q)

        for n_r, n_c, n_dir in getNeighbours(curr_r, curr_c, curr_dir):
            n_dir = Direction.toIdx(n_dir)

            if visited[n_r][n_c][n_dir]:
                continue

            turning_cost = 0 if (n_dir == curr_dir) else 1000
            new_cost = curr_cost + 1 + turning_cost

            visited[n_r][n_c][n_dir] = True

            distB[n_r][n_c] = min(distB[n_r][n_c], new_cost)

            heapq.heappush(q, (new_cost, n_r, n_c, n_dir))

    # Adding the minimum distance from SRC to (r,c) & DEST to (r,c)
    # yields a score for each tile which contains the MIN of ALL paths
    # that crossed the tile. If this matches* the score from Part 1,
    # this tile is a member of at least one of the paths.
    sum_dist = [[distA[r][c] + distB[r][c] - min_cost for c in range(m)] for r in range(n)]

    n = sum(
        # FIXME: Due to double-counting, items not @ a turn have
        # an additional 1000.
        sum_dist[r][c] == 0 or sum_dist[r][c] == 1000
        for r in range(n)
        for c in range(m)
    )

    return n

with open("input.txt", 'r') as fp:
    data = fp.read()
    data = data.split('\n')
    grid = [list(d) for d in data]

    def getSourceandDest(grid: List[List[str]]) -> tuple[Point, Point]:
        n, m = len(grid), len(grid[0])

        src = dest = (0, 0)

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "S":
                    src = (r, c)
                
                if grid[r][c] == "E":
                    dest = (r, c)

        return src, dest

    src, dest = getSourceandDest(grid)

    # Now, we can consider them as normal tiles.
    grid[src[0]][src[1]] = "."
    grid[dest[0]][dest[1]] = "."

    # 95444
    ans1 = Part1(grid, src, dest)
    print(ans1)

    ans2 = Part2(grid, src, dest, ans1)
    print(ans2)



    