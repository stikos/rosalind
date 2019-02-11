# my solution
if __name__ == '__main__':
    input_lines = open('rosalind_prot.txt', 'r').read()

    table = '''UUU F      CUU L      AUU I      GUU V
            UUC F      CUC L      AUC I      GUC V
            UUA L      CUA L      AUA I      GUA V
            UUG L      CUG L      AUG M      GUG V
            UCU S      CCU P      ACU T      GCU A
            UCC S      CCC P      ACC T      GCC A
            UCA S      CCA P      ACA T      GCA A
            UCG S      CCG P      ACG T      GCG A
            UAU Y      CAU H      AAU N      GAU D
            UAC Y      CAC H      AAC N      GAC D
            UAA Stop   CAA Q      AAA K      GAA E
            UAG Stop   CAG Q      AAG K      GAG E
            UGU C      CGU R      AGU S      GGU G
            UGC C      CGC R      AGC S      GGC G
            UGA Stop   CGA R      AGA R      GGA G
            UGG W      CGG R      AGG R      GGG G'''.split('   ')

    while '' in table:
        table.remove('')

    table = dict([x.split() for x in table])
    protein = ""

    while input_lines:
        triplet = input_lines[:3]
        if table[triplet] == 'Stop':
            break
        else:
            protein += table[triplet]
            input_lines = input_lines[3:]

    print(protein)
    
# best solution
# -
