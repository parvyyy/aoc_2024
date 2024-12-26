from itertools import chain
from collections import Counter

def plutonian_pebbles(l: list[int]):
    def on_blink(l: list[int]):
        def blink(n: int):
            if n == 0:
                return [1]
            
            # Even number of digits
            n_dig = len(str(n))
            if n_dig % 2 == 0:
                n, n_dig = str(n), int(n_dig / 2)

                l, r = int(n[:n_dig]), int(n[n_dig:])
                return [l, r]
            else:
                return [n * 2024]

        # Flattens the 2D array into a 1D array. Was unable to find a nice way
        # to flatten ['3', ['1', '2']] into ['3', '1', '2'], hence isolated values
        # are wrapped in '[]'.
        l = list(chain.from_iterable(map(lambda x: blink(x), l)))

        

        return l

    for i in range(75):
        l = on_blink(l)
        print(i, l)
    
    print(len(l))

# To optimise, we must not flat map. Instead, the order of the list doesn't
# matter -- simply its length. Hence, we can use a dict / Counter and just find the sum.
def plutonian_pebbles_optimised(l: list[int]):
    data = Counter(l)
    for _ in range(75):
        # Must have two seperate counters. This ensures there isn't any concurrent modification.
        # This also allows us to do multiple calculations in one-step by accounting for all iterations.
        stones = Counter()
        for n, num_stones in data.items():
            if n == 0:
                stones[1] += num_stones
                continue
            
            # Even number of digits
            n_dig = len(str(n))
            if n_dig % 2 == 0:
                n, n_dig = str(n), int(n_dig / 2)

                l, r = int(n[:n_dig]), int(n[n_dig:])
                
                stones[l] += num_stones
                stones[r] += num_stones
            else:
                stones[n * 2024] += num_stones

        data = stones
    
    print(sum(stones.values()))


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        plutonian_pebbles_optimised([int(x) for x in f.read().split()])
