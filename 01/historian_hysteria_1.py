
def difference_in_lists(l1: list, l2: list) -> int:
  sum = 0
  for a, b in zip(l1, l2):
    sum += abs(a - b)

  return sum

def main():
  with open('input.txt', 'r') as file:
    l1, l2 = [], []
    for line in file:
      v1, v2 = line.split()
      l1.append(int(v1))
      l2.append(int(v2))

    res = difference_in_lists(sorted(l1), sorted(l2))

    print(f"The answer is {res}")

if __name__ == '__main__':
    main()