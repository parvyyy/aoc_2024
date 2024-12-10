def main():
  keyword = "XMAS"
  with open("input.txt", "r") as f:
    wordlist = [list(line.strip()) for line in f.readlines()]
    tot_row, tot_col = len(wordlist), len(wordlist[0])

    sum  = 0
    for (row, line) in enumerate(wordlist):
      for (col, letter) in enumerate(line):
        if letter != "X":
          continue

        def num_xmas(row, col):
          count = 0
          # Horizontal right
          if 0 <= col <= tot_col - len(keyword):
            word = "".join(wordlist[row][col + i] for i in range(len(keyword)))
            count += keyword == word

          # Horizontal left
          if len(keyword) - 1 <= col < tot_col:
            word = "".join(wordlist[row][col - i] for i in range(len(keyword)))
            count += keyword == word

          # Vertical down
          if 0 <= row <= tot_row - len(keyword):
            word = "".join([wordlist[row + i][col] for i in range(len(keyword))])
            count += keyword == word

          # Vertical up
          if len(keyword) - 1 <= row < tot_row:
            word = "".join([wordlist[row - i][col] for i in range(len(keyword))])
            count += keyword == word

          # Diagonal down right
          if 0 <= row <= tot_row - len(keyword) and 0 <= col <= tot_col - len(keyword):
            word = "".join([wordlist[row + i][col + i] for i in range(len(keyword))])
            count += keyword == word

          # Diagonal down left
          if 0 <= row <= tot_row - len(keyword) and len(keyword) - 1 <= col < tot_col:
            word = "".join([wordlist[row + i][col - i] for i in range(len(keyword))])
            count += keyword == word

          # Diagonal up right
          if len(keyword) - 1 <= row < tot_row and 0 <= col <= tot_col - len(keyword):
            word = "".join([wordlist[row - i][col + i] for i in range(len(keyword))])
            count += keyword == word

          # Diagonal up left
          if len(keyword) - 1 <= row < tot_row and len(keyword) - 1 <= col < tot_col:
            word = "".join([wordlist[row - i][col - i] for i in range(len(keyword))])
            count += keyword == word

          return count

        sum += num_xmas(row, col)

  print(sum)



if __name__ == "__main__":
    main()