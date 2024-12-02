from enum import Enum
class Status(Enum):
  INC = 1,
  DEC = -1

def is_level_safe_basic(line: list[int]) -> bool:
  if len(line) == 0 or len(line) == 1:
    return True

  status = None
  diffs = [x - y for x, y in zip(line, line[1:])]

  for diff in diffs:
    if not status:
      status = Status.INC if diff > 0 else Status.DEC

    if (status == Status.INC and diff < 0) or (status == Status.DEC and diff > 0):
      return False

    diff = abs(diff)
    # diff must be {1, 2, 3}
    if diff <= 0 or diff >= 4:
      return False

  return True

def is_level_safe_advanced(line: list[int]) -> bool:
  if is_level_safe_basic(line):
    return True

  # Selectively remove one element and check if the level is safe
  for i in range(len(line)):
    # Removes the ith element
    new_line = line[:i] + line[i+1:]

    if is_level_safe_basic(new_line):
      return True


  return False


def main():
  with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.split() for line in lines]
    lines = [[int(x) for x in line] for line in lines]

    safe_count = 0
    for line in lines:
      if is_level_safe_basic(line):
        safe_count += 1

    print(f"The answer for Part 1 is {safe_count}")

    safe_count = 0
    for line in lines:
      if is_level_safe_advanced(line):
        safe_count += 1

    print(f"The answer for Part 2 is {safe_count}")

if __name__ == '__main__':
    main()