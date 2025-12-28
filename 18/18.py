from typing import List
from collections import deque

type Vec2 = tuple[int, int]

def Part1(grid: List[List[str]]) -> int:
    n = len(grid)

    def getNeighbours(v: Vec2) -> List[Vec2]:
        def isValid(r, c):
            return 0 <= r < n and 0 <= c < n
        
        r, c = v

        neighbours = []
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not isValid(nr, nc):
                continue

            if grid[nr][nc] == ".":
                neighbours.append((nr, nc))

        return neighbours

    # Standard BFS, tracking the path length.
    q = deque()
    q.append((0, 0, 0))

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    min_dist = 0
    while q:
        curr_dist, curr_r, curr_c = q.popleft()

        if curr_r == curr_c == (n - 1):
            min_dist = curr_dist
            break

        for nr, nc in getNeighbours((curr_r, curr_c)):
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True

            n_dist = curr_dist + 1
            q.append((n_dist, nr, nc))

    return min_dist

def Part2(points: List[Vec2], n = 71):
    # Use binary search to adjust `k`, to find
    # where the `min_dist` is changes from
    # a sol to a non-sol.
    lo, hi = 0, len(points) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        grid = create(points, n, mid)
        min_dist = Part1(grid)

        # At this point, `lo` represents
        # the 'k' val which still has a sol.
        # 'hi' has the 'k' value which produces
        # no solutions. 
        #
        # However, this means from 0 .. hi (non-inc.)
        # Therefore, the point at `hi - 1` cut
        # it off.
        if lo == hi - 1:
            return hi, points[hi - 1]

        if not min_dist:
            hi = mid
        else:
            lo = mid

    return (-1, -1)
    
def create(points: List[Vec2], n: int = 71, k: int = 1024):
    grid = [["." for _ in range(n)] for _ in range(n)]

    # Set the first k obstacles
    for pc, pr in points[:k]:
        grid[pr][pc] = "#" 
    
    return grid

with open("input.txt", 'r') as fp:#
    data = fp.read()
    data = data.split('\n')
    data = [d.split(',') for d in data]
    points: List[Vec2] = [(int(d[0]), int(d[1])) for d in data]

    n, k = 71, 1024
    grid = create(points, n, k)

    ans1 = Part1(grid)
    print(ans1)

    k_opt, ans2 = Part2(points, n)
    print(k_opt, ans2)