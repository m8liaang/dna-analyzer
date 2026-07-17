from valid_DNA_sequence import valid
from base_counter import base_counter
from gc_calculator import GC_content
from complementary_generator import DNA_complement
from mRNA_generator import RNA_generator

def analyzer():
  
  DNA_string = input("Enter a DNA sequence: ")

  sequence = valid(DNA_string)

  if sequence is False:
    print("DNA sequence is not valid.")
  else:
    base_counter(sequence)
    GC_content(sequence)
    DNA_complement(sequence)
    RNA_generator(sequence)
