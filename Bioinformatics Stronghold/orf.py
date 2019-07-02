# my solution
import re

aa = "UUU F,CUU L,AUU I,GUU V,UUC F,CUC L,AUC I,GUC V,UUA L,CUA L,AUA I,GUA V,UUG L,CUG L,AUG M,GUG V,UCU S,CCU P," \
     "ACU T,GCU A,UCC S,CCC P,ACC T,GCC A,UCA S,CCA P,ACA T,GCA A,UCG S,CCG P,ACG T,GCG A,UAU Y,CAU H,AAU N,GAU D," \
     "UAC Y,CAC H,AAC N,GAC D,CAA Q,AAA K,GAA E,CAG Q,AAG K,GAG E,UGU C,CGU R,AGU S,GGU G,UGC C,CGC R,AGC S,GGC G," \
     "CGA R,AGA R,GGA G,UGG W,CGG R,AGG R,GGG G,UAA Stop,UGA Stop,UAG Stop".split(',')
aa = dict(map(lambda x: x.split(' '), aa))

start_codon = "AUG"
stop_codons = ["UAA", "UGA", "UAG"]


def reverse_complement(dna):
    lookup = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([lookup[c] for c in reversed(dna)])

def find_prot(dna):
    output = []
    start_points = [s.start() for s in re.finditer(start_codon, dna)]
    for point in start_points:
        protein = ""
        for i in range(point, len(dna), 3):
            if len(dna[i: i + 3]) == 3:
                if aa[dna[i: i + 3]] != "Stop":
                    protein += aa[dna[i: i + 3]]
                elif aa[dna[i: i + 3]] == "Stop":
                    output.append(protein)
                    break
                else:
                    break

    return output


if __name__ == "__main__":
    input_lines = ''.join(open('rosalind_orf.txt', 'r').readlines()[1:]).replace('\n','')

    final_output = set(find_prot(input_lines.replace('T', 'U')) +
                       find_prot(reverse_complement(input_lines).replace('T', 'U')))

    print(*final_output, sep='\n')