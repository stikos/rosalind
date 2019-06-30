# my solution

aa = "UUU F,CUU L,AUU I,GUU V,UUC F,CUC L,AUC I,GUC V,UUA L,CUA L,AUA I,GUA V,UUG L,CUG L,AUG M,GUG V,UCU S,CCU P," \
     "ACU T,GCU A,UCC S,CCC P,ACC T,GCC A,UCA S,CCA P,ACA T,GCA A,UCG S,CCG P,ACG T,GCG A,UAU Y,CAU H,AAU N,GAU D," \
     "UAC Y,CAC H,AAC N,GAC D,CAA Q,AAA K,GAA E,CAG Q,AAG K,GAG E,UGU C,CGU R,AGU S,GGU G,UGC C,CGC R,AGC S,GGC G," \
     "CGA R,AGA R,GGA G,UGG W,CGG R,AGG R,GGG G,UAA Stop,UGA Stop,UAG Stop".split(',')
aa = dict(map(lambda x: x.split(' '), aa))
aa_cardinality = {}
for k, v in aa.items():
    if v not in aa_cardinality:
        aa_cardinality[v] = 1
    else:
        aa_cardinality[v] += 1

if __name__ == "__main__":
    counter = aa_cardinality["Stop"]
    input_lines = open('rosalind_mrna.txt', 'r').read().strip("\n")
    for aa in input_lines:
        counter *= aa_cardinality[aa]
        # if counter > 1000000:
        #     counter = counter % 1000000
    print(counter % 1000000)

