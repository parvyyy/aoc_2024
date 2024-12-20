from itertools import combinations
from collections import defaultdict

def resonant_collinearity(input: list[str]):
  """
    Have a hashmap w/ the key's as the frequencies (i.e. 'a', 'A', '0'), and their
    positions as the values in a list.

    Then create all the possible combinations of pairs of 2.
    For each pair, use vector math [v1 - (v2 - v1)] & [v2 + (v2 - v1)] to find
    the 2 collinear points.

    Add to a set. -- this means we can later compute. If we do it at the same time,
    mulitple #'s could appear on the same spot and cause double counting. We want the
    locations to be unique, hence a set.

    Filter the set based on whether it's a valid location on the board.

    Return the length of the set.
  """

  # Must strip the newline character from the end of each line.
  # https://www.reddit.com/r/adventofcode/comments/1hg0dza/2024_day_8_part_1_python_help_works_on_example/
  r, c = len(input), len(input[0].strip())

  def in_bounds(r0, c0):
    return 0 <= r0 < r and 0 <= c0 < c

  frequencies = defaultdict(list)

  for i, line in enumerate(input):
    for j, char in enumerate(line):
      if char.isalnum():
        frequencies[char].append((i, j))

  antinodes = set()
  for v in frequencies.values():
    pairs = list(combinations(v, 2))

    for v1, v2 in pairs:
      diff = (v2[0] - v1[0], v2[1] - v1[1])

      # Part 1
      # antinodes.add((v1[0] - diff[0], v1[1] - diff[1]))
      # antinodes.add((v2[0] + diff[0], v2[1] + diff[1]))

      # Part 2
      # Each antenna will now have an antinode on it.
      while in_bounds(*v1):
        antinodes.add(v1)
        v1 = (v1[0] - diff[0], v1[1] - diff[1])

      while in_bounds(*v2):
        antinodes.add(v2)
        v2 = (v2[0] + diff[0], v2[1] + diff[1])

  print(len(antinodes))

  """
  Edits for Part 2:
    Continue adding / subtracting (v2- v1) to the frequencies while
    the result is still in bounds.

    No longer able to filter afterwards as we need to continue adding
    until we reach the end of the board -- cannot know how many iterations.
  """

if __name__ == "__main__":
  with open("input.txt", 'r') as f:
    resonant_collinearity(f.readlines())