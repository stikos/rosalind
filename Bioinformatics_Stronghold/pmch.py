# my solution
from fasta_in import get_input
from math import factorial

if __name__ == '__main__':
    line = get_input('rosalind_pmch.txt')[0]
    n = line.count('A')
    m = line.count('C')
    print(factorial(n) * factorial(m))