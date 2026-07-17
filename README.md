# DNA Analyzer
A Python text-based DNA analyzer that parses and analyzes an inputted FASTA-formatted DNA sequence.

## Features
| Component | Purpose |
| --- | --- |
| Base Counter |Counts the number of adenine (A), thymine (T), guanine (G), and cytosine (C) bases in the inputted DNA sequence.|
| GC Content Calculator | Calculates the percentage of guanine (G) and cytosine (C) bases in the inputted DNA sequence.|
| Complementary Strand Generator | Generates the complementary strand of the inputted DNA sequence. |
| mRNA Strand Generator | Converts inputted DNA sequence into its mRNA sequence.|

## Project Structure
```text
dna-analyzer/
├── data/
│   └── demo.ipynb
├── src/
│   ├── base-counter.py
│   ├── gc.py
│   ├── complementary.py
│   ├── mRNA.py
└── README.md
```
