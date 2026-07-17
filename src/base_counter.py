# DNA Base Counter

def base_counter(sequence):
  A_count, G_count, C_count, T_count = 0, 0, 0, 0

  for letter in sequence:
    if letter == 'A':
      A_count += 1
    elif letter =='G':
      G_count += 1
    elif letter == 'C':
      C_count += 1
    else:
      T_count += 1
    
  return print(f"\nBase Counts:\nA: {A_count}, G: {G_count}, C: {C_count}, T: {T_count}")
