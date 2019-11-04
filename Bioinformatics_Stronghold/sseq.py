# my solution
from fasta_in import get_input

if __name__ == '__main__':
    bpairs, check = get_input('rosalind_sseq.txt')

    res = [bpairs.index(check[0]) + 1]
    for base in check[1:]:
        temp_old = res[-1]
        temp = bpairs[temp_old:].index(base)
        res.append(temp + temp_old + 1)

    print(*res, sep=' ')