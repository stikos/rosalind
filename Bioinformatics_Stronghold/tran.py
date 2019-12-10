# my solution
from fasta_in import get_input

groups = {'purines': ['A', 'G'], 'pyramidines': ['C', 'T']}

if __name__ == '__main__':
    strs = get_input('rosalind_tree.txt')

    print(strs[0], strs[1])

    transitions = sum([1 for i in range(len(strs[0])) if strs[0][i] != strs[1][i]
                       and ((strs[0][i] in groups['purines'] and strs[1][i] in groups['purines'])
                       or (strs[0][i] in groups['pyramidines'] and strs[1][i] in groups['pyramidines']))])

    transversions = sum([1 for i in range(len(strs[0])) if strs[0][i] != strs[1][i]
                         and ((strs[0][i] in groups['purines'] and strs[1][i] in groups['pyramidines'])
                         or (strs[0][i] in groups['pyramidines'] and strs[1][i] in groups['purines']))])

    print("%.11f" % (transitions/transversions))


# elegant, fast solution
from from itertools import izip

def transitionTransversionRatio8(s1, s2):
    trans = {"A":"G", "G":"A", "T":"C", "C":"T"}
    mut = [
             't' if trans[b1] is b2 else 'f'
                 for b1, b2 in izip(s1,s2)
                     if b1 is not b2
    ]

    return mut.count('t') / float(mut.count('f'))