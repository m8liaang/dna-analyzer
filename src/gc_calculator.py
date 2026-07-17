# GC Content Calculator

def GC_content(sequence):
  G_counts = sequence.count('G')
  C_counts = sequence.count('C')

  GC_content = ((G_counts + C_counts) / len(sequence)) * 100

  return print(f"\nGC Content: {round(GC_content, 2)}%")
