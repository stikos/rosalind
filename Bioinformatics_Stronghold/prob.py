# my solution
from math import log10

if __name__ == '__main__':
    bpairs, probs = open('rosalind_sseq.txt', 'r').read().split("\n")[0:2]
    probs = list(map(float, probs.split(' ')))

    final = ""
    for prob in probs:
        res = 0
        for bp in bpairs:
            if bp in ['G', 'C']:
                res += log10(prob/2)
            else:
                res += log10((1-prob)/2)
        final += "{0:.3f}".format(res) + ' '
    print(final)