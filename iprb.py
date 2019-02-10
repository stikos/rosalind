# my solution
from itertools import combinations

if __name__ == '__main__':
    k, m, n = list(map(int, open('rosalind_iprb.txt', 'r').read().split()))

    # k: dominant, m: hetero, n: recessive
    print((len(list(combinations(range(k), 2))) + k * m + k * n + 0.75 * len(
        list(combinations(range(m), 2))) + 0.5 * m * n) /
          (len(list(combinations(range(k), 2))) + k * m + k * n + len(list(combinations(range(m), 2))) + m * n +
           len(list(combinations(range(n), 2)))))


# best solution
# using the complementary probability of getting no dominant alleles
def firstLaw(k, m, n):
    N = float(k + m + n)
    return 1 - 1 / N / (N - 1) * (n * (n - 1) + n * m + m * (m - 1) / 4.)
