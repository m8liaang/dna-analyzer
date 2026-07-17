# mRNA Sequence Generator

def RNA_generator(sequence):
  allowed_characters = {'A', 'G', 'C', 'T'}

  for char in sequence:
    new_sequence = sequence.replace('T', 'U')

  return print(f'\nmRNA strand: {new_sequence}')
