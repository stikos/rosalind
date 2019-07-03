# my solution
# -
# best solution
from scipy.misc import comb

if __name__ == '__main__':
    k, n = list(map(int, open('rosalind_lia.txt', 'r').read().split()))
    t = 2 ** k
    print(round(sum([comb(t, i, 1) * 0.25 ** i * 0.75 ** (t - i) for i in range(n, t + 1)]), 3))


