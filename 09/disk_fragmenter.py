from itertools import zip_longest
def disk_fragmenter(input: str):
  """
    Split the input into two halves - ::2 and 1::2
    Do an enumerate zip with both halves

    Make the file-block string resemble
    '00...111...2...333.44.5555.6666.777.888899'

    Iterate through the file-block, noting the index.
    Store the end_index.
    If the value is '.', replace it with the value at
    the end_index.

    Move the end_index -= 1

    Continue until the index reaches the end_index.

    Calculate the checksum of the new file-block string.

    CHANGES:
    Store numbers in a list instead of a string. This is as in a string, the
    # digits can not be determined.
  """

  file_block = []
  for (f_id, (file_count, free_space)) in enumerate(zip_longest(input[::2], input[1::2], fillvalue="0")):
    for _ in range(int(file_count)):
      file_block.append(str(f_id))

    for _ in range(int(free_space)):
      file_block.append('.')

  # Part 1
  # end_index = len(file_block) - 1
  # for (i, char) in enumerate(file_block):
  #   while file_block[end_index] == '.':
  #     end_index -= 1

  #   if i >= end_index:
  #     break

  #   if char == '.':
  #     file_block = file_block[:i] + [file_block[end_index]] + file_block[i+1:]

  #     file_block[end_index] = '.'
  #     end_index -= 1

  # Part 2
  """
    Find length of first continguous '.' sequence.
    Find length of last continguous number sequence.

    If the length of the # seq < len of '.' sequence, replace.
    Otherwise, continue to the previous number sequence.

    That means we need to capture both continguous # seq and '.' seq.
    Also, we need to make sure that if the lengths are not the same, the extra
    spots are padded with '.'.

    Use a while loop instead for more control. This is because we remain at the
    same '.' seq until it is fulfilled.

    CHANGES:
    Store the (start_free, end_free) in a list -- not set to preserve order.
    Go through contiguous seq of #'s from the back. Find the smallest segment
    they fit in to. Replace them.
  """
  # Part 2
  free_spaces = []

  start_free = end_free = 0
  for (i, v) in enumerate(file_block):
    if i < end_free:
      continue

    while i < len(file_block) and file_block[i] != '.':
      i += 1
    start_free = i

    while i < len(file_block) and file_block[i] == '.':
      i += 1
    end_free = i

    free_spaces.append((start_free, end_free))

  free_spaces = free_spaces[:-1]
  new_file_block = file_block[::]

  start_file = end_file = len(file_block)
  for (i, v) in reversed(list(enumerate(file_block))):
    if i > start_file:
      continue
    
    while i >= 0 and file_block[i] == '.':
      i -= 1
    end_file = i

    while i >= 0 and file_block[i] == file_block[end_file]:
      i -= 1
    start_file = i

    for (j, (start, end)) in enumerate(free_spaces):
      diff = (end - start) - (end_file - start_file)
      if diff >= 0:
          # Move entire file into free space & padd extra space with '.'
        new_file_block[start:end] = file_block[start_file+1:end_file+1] + ['.'] * diff

        # Replace original file with '.'
        new_file_block[start_file+1:end_file+1] = ['.'] * (end_file - start_file)

        # Remove this as a free-space candidate & replace it with the new free_space.
        free_spaces[j] = (end - diff, end)

        break
  
  # Checksum calculation
  checksum = 0
  for (i, v) in enumerate(new_file_block):
    if v != '.':
      checksum += (i * int(v))

  print(checksum)


if __name__ == "__main__":
  with open("input.txt", 'r') as f:
    disk_fragmenter(f.read())