from collections import Counter
import pprint

def difference_in_lists(l1: list, l2: list) -> int:
  sum = 0
  for a, b in zip(l1, l2):
    sum += abs(a - b)

  return sum

def determine_similarity(l1: list, l2: list) -> int:
  location_counts = Counter(l2)

  sum = 0
  for v in l1:
    if v in location_counts:
      sum += (v * location_counts[v])

  return sum

def main():
  with open('input.txt', 'r') as file:
    l1, l2 = [], []
    for line in file:
      v1, v2 = line.split()
      l1.append(int(v1))
      l2.append(int(v2))


    res_1 = difference_in_lists(sorted(l1), sorted(l2))
    res_2 = determine_similarity(l1, l2)

    print(f"The answer for Part 1 is {res_1}")
    print(f"The answer for Part 2 is {res_2}")

if __name__ == '__main__':
    main()