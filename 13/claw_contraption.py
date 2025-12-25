from typing import List
import re
import numpy as np

"""
The following machine:
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400
can be represented as a pair of simultaneous equations.

Let a0, b0 represent the # of presses of Button A, B.
Then,
    94 * a0 + 22 * b0 = 8400
    34 * a0 + 67 * b0 = 5400
Solving this yields a0 = 80, b0 = 40 as req.

There is only one solution, hence it IS the minimum.
"""

def Part1(data):
    total = 0
    for X, Y, Z in data:
        coeff = [
            [X[0], Y[0]], 
            [X[1], Y[1]]
        ]

        sol = np.linalg.solve(coeff, Z)

        # To correctly round due to float inprecision.
        a0, b0 = sol[0], sol[1]
        a0, b0 = round(a0, 2), round(b0, 2)

        def isWhole(n):
            return int(n) == float(n)

        # Ensures the solutions are a valid amnt
        # of presses (i.e. non-fractional)
        if not (isWhole(a0) and isWhole(b0)):
            continue

        if not (0 < a0 < 100 and 0 < b0 < 100):
            continue

        # Pressing A costs 3 tokens, pressing B costs 1.
        total += (3 * a0) + (1 * b0)
    
    return total

def Part2(data):
    total = 0
    for X, Y, Z in data:
        coeff = [
            [X[0], Y[0]], 
            [X[1], Y[1]]
        ]

        res = [
            Z[0] + 10000000000000,
            Z[1] + 10000000000000
        ]

        sol = np.linalg.solve(coeff, res)

        # To correctly round due to float inprecision.
        a0, b0 = sol[0], sol[1]
        a0, b0 = round(a0, 2), round(b0, 2)

        def isWhole(n):
            return int(n) == float(n)

        # Ensures the solutions are a valid amnt
        # of presses (i.e. non-fractional)
        if not (isWhole(a0) and isWhole(b0)):
            continue

        # Pressing A costs 3 tokens, pressing B costs 1.
        total += (3 * a0) + (1 * b0)
    
    return total

type Vec2 = tuple[int, int]

with open("input.txt", 'r') as fp:
    data = fp.read()
    data = data.split('\n\n')
    data = [d.split('\n') for d in data]

    def toMachine(data: List[str]):
        m1 = re.match(r"Button A: X\+(\d+), Y\+(\d+)", data[0])
        m2 = re.match(r"Button B: X\+(\d+), Y\+(\d+)", data[1])
        m3 = re.match(r"Prize: X=(\d+), Y=(\d+)", data[2])

        X: Vec2 = [int(v) for v in m1.groups()]
        Y: Vec2 = [int(v) for v in m2.groups()]
        Z: Vec2 = [int(v) for v in m3.groups()]

        return X, Y, Z

    data = [toMachine(d) for d in data]

    ans1 = Part1(data)
    print(ans1)

    ans2 = Part2(data)
    print(ans2)
