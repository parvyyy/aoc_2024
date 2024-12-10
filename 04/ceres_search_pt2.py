import numpy

def main():
  with open("input.txt", "r") as f:
    keyword = "MAS"

    wordlist = [list(line.strip()) for line in f.readlines()]
    tot_row, tot_col = len(wordlist), len(wordlist[0])

    sum  = 0
    for (row, line) in enumerate(wordlist):
      for (col, letter) in enumerate(line):
        if letter != "M":
          continue

        def num_masX(row, col):
          count = 0

          def diagonalise(matrix):
            d1, d2 = numpy.diag(matrix), numpy.diag(matrix[::-1])[::-1]
            return d1, list([str(x) for x in reversed(d1)]), d2, list([str(x) for x in reversed(d2)])

          # Bottom right matrix
          if 0 <= row <= tot_row - len(keyword) and 0 <= col <= tot_col - len(keyword):
            matrix = [line[col : col + len(keyword)] for line in wordlist[row : row + len(keyword)]]

            d1, d2, d3, d4 = diagonalise(matrix)
            matching_diags = list(filter(lambda d: d == keyword, map(lambda d: "".join(d), [d1, d2, d3, d4])))

            count += len(matching_diags) >= 2

          # Bottom left matrix
          if 0 <= row <= tot_row - len(keyword) and len(keyword) - 1 <= col < tot_col:
            matrix = [line[col - len(keyword) + 1 : col + 1] for line in wordlist[row : row + len(keyword)]]

            d1, d2, d3, d4 = diagonalise(matrix)
            matching_diags = list(filter(lambda d: d == keyword, map(lambda d: "".join(d), [d1, d2, d3, d4])))

            count += len(matching_diags) >= 2

          # Top right matrix
          if len(keyword) - 1 <= row < tot_row and 0 <= col <= tot_col - len(keyword):
            matrix = [line[col : col + len(keyword)] for line in wordlist[row - len(keyword) + 1 : row + 1]]

            d1, d2, d3, d4 = diagonalise(matrix)
            matching_diags = list(filter(lambda d: d == keyword, map(lambda d: "".join(d), [d1, d2, d3, d4])))

            count += len(matching_diags) >= 2

          # Top left matrix
          if len(keyword) - 1 <= row < tot_row and len(keyword) - 1 <= col < tot_col:
            matrix = [line[col - len(keyword) + 1 : col + 1] for line in wordlist[row - len(keyword) + 1 : row + 1]]

            d1, d2, d3, d4 = diagonalise(matrix)
            matching_diags = list(filter(lambda d: d == keyword, map(lambda d: "".join(d), [d1, d2, d3, d4])))

            count += len(matching_diags) >= 2

          return count

        sum += num_masX(row, col)

  # Must half as we double count
  print(sum / 2)

if __name__ == "__main__":
    main()