from typing import List

def Part1(grid: List[List[str]], instructions: List[str]):
    def getRobotPosition(grid: List[List[str]]) -> tuple[int, int]:
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == "@":
                    return (i, j)
        
        return 0, 0

    curr_r, curr_c = getRobotPosition(grid)

    def toVector(instruction: str):
        match (instruction):
            case "^":
                dr, dc = -1, 0
            case ">":
                dr, dc = 0, 1
            case "v":
                dr, dc = 1, 0
            case "<":
                dr, dc = 0, -1
            case _:
                dr, dc = 0, 0
        
        return dr, dc

    for instruction in instructions:
        dr, dc = toVector(instruction)

        def moveRobot(old_r, old_c, new_r, new_c):
            grid[old_r][old_c] = '.'
            grid[new_r][new_c] = "@"
            
            return new_r, new_c

        # Do not move curr, simulate first
        # with a candidate.
        cand_r, cand_c = curr_r + dr, curr_c + dc

        if grid[cand_r][cand_c] == "#":
            continue

        if grid[cand_r][cand_c] == ".":
            curr_r, curr_c = moveRobot(curr_r, curr_c, cand_r, cand_c)
            continue

        if grid[cand_r][cand_c] == "O":
            def getAdjBoxCount(r, c, dr, dc):
                box_len = 1

                while True:
                    next_r, next_c = r + (box_len * dr), c + (box_len * dc)

                    # Boxes cannot be pushed.
                    if (grid[next_r][next_c] == "#"):
                        return 0
                    
                    if (grid[next_r][next_c] == "."):
                        break

                    box_len += 1

                return box_len
        
            # Find length of box chain.
            box_len = getAdjBoxCount(cand_r, cand_c, dr, dc)

            if box_len == 0:
                continue

            curr_r, curr_c = moveRobot(curr_r, curr_c, cand_r, cand_c)

            # Move k boxes in the same dir.
            for i in range(1, box_len + 1):
                cand_r2, cand_c2 = cand_r + (i * dr), cand_c + (i * dc)
                grid[cand_r2][cand_c2] = "O"
            
            continue

    total = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "O":
                total += (100 * i + 1 * j)

    return total


def Part2():
    pass

with open("input.txt") as fp:
    data = fp.read()
    grid, instructions = data.split('\n\n')

    grid = [list(g) for g in grid.split('\n')]
    instructions = filter(lambda c: c != '\n', list(instructions))

    ans1 = Part1(grid, instructions)
    print(ans1)

    ans2 = Part2(grid, instructions)
    print(ans2)
