#!/usr/bin/env python3

# my solution
import re
from prot import make_protein

if __name__ == "__main__":
    input_lines = re.split(r'>Rosalind_[0-9]+\n', open('rosalind_splc.txt', 'r').read())
    input_lines = [x.replace('\n', '') for x in input_lines[1:]]

    dna = input_lines[0]
    introns = input_lines[1:]

    for x in introns:
        dna = dna.replace(x, '')

    make_protein(dna.replace('T', 'U'))

