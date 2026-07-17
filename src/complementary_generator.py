# Complementary Strand Generator

def DNA_complement(sequence):
  complements = {
      'A' : 'T',
      'G' : 'C',
      'C' : 'G',
      'T' : 'A'
  }
  allowed_characters = {'A', 'G', 'C', 'T'}
  DNA_complements = ''

  for char in sequence:
    for key, value in complements.items():
      if key == char:
        DNA_complements += str(complements[f'{key}'])

  return print(f'\nComplementary Strand: {DNA_complements}')
