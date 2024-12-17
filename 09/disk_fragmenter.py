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
  end_index = len(file_block) - 1
  for (i, char) in enumerate(file_block):
    while file_block[end_index] == '.':
      end_index -= 1

    if i >= end_index:
      break

    if char == '.':
      file_block = file_block[:i] + [file_block[end_index]] + file_block[i+1:]

      file_block[end_index] = '.'
      end_index -= 1


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
  """
  # Part 2
  # i, end_index = 0, len(file_block) - 1
  # while i < end_index:
  #   while file_block[i] != '.':
  #     i += 1

  #   start_free = i

  #   while file_block[i] == '.':
  #     i += 1

  #   end_free = i

  #   start_file, end_file = 0, end_index

  #   while end_free - start_free < end_file - start_file:
  #     while file_block[end_index] == '.':
  #       end_index -= 1

  #     end_file, v = end_index + 1, file_block[end_index]

  #     # We must look for !v instead of '.' as there may be 0 free space between.
  #     while file_block[end_index] == v:
  #       end_index -= 1

  #     start_file = end_index + 1


  #   diff = (end_free - start_free) - (end_file - start_file)

  #   # Move entire file into free space & padd extra space with '.'
  #   file_block[start_free:end_free] = file_block[start_file:end_file] + ['.'] * diff

  #   # Replace original file with '.'
  #   file_block[start_file:end_file] = ['.'] * (end_file - start_file)


  # print(file_block)

  # Checksum calculation
  checksum = 0
  for (i, v) in enumerate(file_block[:end_index+1]):
    if v != '.':
      checksum += (i * int(v))

  print(checksum)


if __name__ == "__main__":
  with open("small_input.txt", 'r') as f:
    disk_fragmenter(f.read())