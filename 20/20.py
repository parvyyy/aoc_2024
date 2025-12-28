
import math
from typing import List
from collections import deque

def Part1(grid: List[List[str]], src: Point, dest: Point, k: int):
    n, m = len(grid), len(grid[0])

    src_r, src_c = src
    dest_r, dest_c = dest

    def getNeighbours(r: int, c: int) -> List[int]:
        if grid[r][c] == "#":
            return []
        

        neighbours = []
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if grid[nr][nc] == ".":
                neighbours.append((nr, nc))

        return neighbours
    
    # BFS w/ min-path
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([(src_r, src_c)])

    visited[src_r][src_c] = True

    min_path = None
    while q:
        path = q.popleft()
        curr_r, curr_c = path[-1]

        if curr_r == dest_r and curr_c == dest_c:
            min_path = path
            break

        for nr, nc in getNeighbours(curr_r, curr_c):
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True

            q.append((path + [(nr, nc)]))

    def dist(p1: Point, p2: Point) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    cheat_count = 0

    # FIXME: Optimize this to reduce the search space.
    #        Rather than inspecting every combination
    #        of points, only do those in a radius of 'k'
    #        around each point. 
    for i, p1 in enumerate(min_path):
        for j, p2 in enumerate(min_path):
            if i > j:
                continue

            d = dist(p1, p2)
            
            # The cheat must take 'k' or less steps.
            if d <= k:
                # The saved time is the distance in
                # the path index. This costs `d` steps.
                cheat = (j - i) - d

                if cheat >= 100:
                    cheat_count += 1

    return cheat_count

type Point = tuple[int, int]

with open("input.txt", 'r') as fp:#
    data = fp.read()
    data = data.split('\n')
    grid = [list(d) for d in data]

    def getSourceAndDest(grid: List[List[str]]) -> tuple[Point, Point]:
        n, m = len(grid), len(grid[0])

        src = dest = None
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "S":
                    src: Point = r, c
                
                if grid[r][c] == "E":
                    dest: Point = r, c

        return src, dest
    
    src, dest = getSourceAndDest(grid)

    # Remove special markings
    grid[src[0]][src[1]] = "."
    grid[dest[0]][dest[1]] = "."

    # 1395
    ans1 = Part1(grid, src, dest, k = 2)
    print(ans1)

    # 993178
    # NOTE: There was no need for a custom sol.
    #       to Part2 - it simply required modifying
    #       the `k` value.
    ans2 = Part1(grid, src, dest, k = 20)
    print(ans2)