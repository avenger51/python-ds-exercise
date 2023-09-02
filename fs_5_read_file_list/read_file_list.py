def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

  #solution:
    with open(filename) as f:   #with closes the file....?
        for line in f:
            # remove newline at end of line!
            line = line.strip()
            print(f"- {line}")

  #  try:
  #          with open(filename, 'r') as file:
  #              for line in file:
  #                  stripped_line = line.strip()
  #              if stripped_line:
  #                  print(f"- {stripped_line}")
  #  except FileNotFoundError:
  #          raise FileNotFoundError(f"File '{filename}' not found.")