# my solution
if __name__ == '__main__':
    input_pairs = list(map(int, open('rosalind_iev.txt', 'r').read().split()))
    print(sum([(input_pairs[0] + input_pairs[1] + input_pairs[2]) * 2,
              input_pairs[3] * 1.5,
              input_pairs[4]]))

# best solution
