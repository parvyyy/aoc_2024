import re

def main():
  with open("input.txt") as f:
    memory = f.read()

    # Part 1
    if m := re.findall(r'mul\((\d+),(\d+)\)', memory):
      res = sum(map(lambda x: int(x[0]) * int(x[1]), m))
      print(res)

    # Part 2
    # Different approach instead of regex'inh do() and don't()
    filtered_memory = [mem.split("don't()") for mem in memory.split("do()")]

    res = 0
    for instruction in filtered_memory:
      # We only consider the first, as this is between do() and don't()
      instruction = instruction[0]

      if m := re.findall(r'mul\((\d+),(\d+)\)', instruction):
        res += sum(map(lambda x: int(x[0]) * int(x[1]), m))
    print(res)

if __name__ == "__main__":
    main()