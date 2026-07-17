def valid(sequence):

  allowed_characters = {'A', 'G', 'C', 'T'}

  sequence = sequence.upper().replace(" ", "")

  for char in sequence:
    if char not in allowed_characters:
      return False

  return sequence
