import math
import re

def Part1(trajectories: tuple[tuple[int, int], tuple[int, int]]):
    n_steps = 100
    w, h = 101, 103

    final_positions = []

    for trajectory in trajectories:
        pc, pr = trajectory[0]
        vc, vr = trajectory[1]

        dc = pc + (n_steps * vc)
        dr = pr + (n_steps * vr)

        dc = dc % w
        dr = dr % h

        final_positions.append((dr, dc))

    quad = [0 for _ in range(4)]

    def toQuad(dr, dc):
        if (0 <= dc < (w - 1) / 2 and 0 <= dr < (h - 1) / 2):
            return 0
        
        if (0 <= dc < (w - 1) / 2 and (h + 1) / 2 <= dr < h):
            return 1
        
        if ((w + 1) / 2 <= dc < w and 0 <= dr < (h - 1) / 2):
            return 2
        
        if ((w + 1) / 2 <= dc < w and (h + 1) / 2 <= dr < h):
            return 3
        
        return -1

    for dr, dc in final_positions:
        q = toQuad(dr, dc)

        if q == -1:
            continue

        quad[q] += 1

    prod = math.prod(quad)

    return prod

# TODO: Unsure how to determine if the position
#       resembles a 'picture of a christmas
#       tree'
def Part2(data):
    pass

with open("input.txt", 'r') as fp:
    data = fp.read()
    data = data.split('\n')

    def toPosVector(data: str):
        m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", data)
        px, py, vx, vy = m.groups()

        return (int(px), int(py)), (int(vx), int(vy))
    
    data = [toPosVector(d) for d in data]

    ans1 = Part1(data)
    print(ans1)

    ans2 = Part2(data)
    print(ans2)