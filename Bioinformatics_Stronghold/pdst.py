from os import sep
from fasta_in import get_input
strings_in = get_input("rosalind_pdst.txt")

table = [len(strings_in)*[0] for i in range(len(strings_in))]
for i, string_prim in enumerate(strings_in):
    for j, string_check in enumerate(strings_in):
        table[i][j] = sum([x!=y for x,y in zip(string_prim, string_check)])/len(string_prim)

for line in table:
    print(' '.join(map(str,line)))
