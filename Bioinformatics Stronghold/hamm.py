# my solution
if __name__ == '__main__':
    input_lines = open('rosalind_hamm.txt', 'r').readlines()
    print(sum([int(i != j) for i, j in zip(input_lines[0], input_lines[1])]))

# best solution
# generator, not tuple (zip), great for memory AND faster
import operator
sum(map(operator.ne, s1, s2))