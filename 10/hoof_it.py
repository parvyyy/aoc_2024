import pprint

def hoof_it(topographic_map: list[list[str]]) -> None:
    """
        Ad-hoc DFS for each 'trailhead' -- (0 node)

        Iterating through each element
            Once a 0 is found, start a DFS
                visited[(i, j)] = 1

                if node == 9:
                    Add 1 to the trailhead count.
                    return

                For each neighbouring node:
                    If node is 0 + 1:
                        Rerun the DFS

                Unset the visited[(i, j)]. This allows it to be used
                by later trailheads or a different path.
            
            Sum the total paths found for this trailhead.
    """

    visited = [[False for _ in range(len(line))] for line in topographic_map]
    r, c = len(topographic_map), len(topographic_map[0])

    def dfs(node: tuple[int, int], endpoints: list[tuple[int, int]]):
        i, j = node

        if topographic_map[i][j] == "9":
            endpoints.append((i, j))
            return

        visited[i][j] = True
        

        for (n_i, n_j) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if n_i < 0 or n_i >= r or n_j < 0 or n_j >= c:
                continue

            if visited[n_i][n_j]:
                continue

            # A node is considered to be connected to another if it is the succeeding value.
            # That is, 1 is connected to 2, 2 connected to 3 etc.
            next = int(topographic_map[i][j]) + 1
            if int(topographic_map[n_i][n_j]) == next:
                dfs((n_i, n_j), endpoints)

        visited[i][j] = False

    total_num_trailheads = 0
    for (i, line) in enumerate(topographic_map):
        for (j, node) in enumerate(line):
            if not visited[i][j] and node == "0":
                # By changing the list to a set, Part 1 is solved too!
                # Part 2 requires a list as we want the total number of paths,
                # even if their endpoint is the same!
                endpoints = []
                dfs((i, j), endpoints)

                total_num_trailheads += len(endpoints)

    print(total_num_trailheads)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        hoof_it([list(c.strip()) for c in f.readlines()])