# my solution
import re
if __name__ == '__main__':
    input_lines = re.split(r'>Rosalind_[0-9]+\n', open('rosalind_cons.txt', 'r').read())
    input_lines = [x.replace('\n', '') for x in input_lines[1:]]
    bases = sorted(list(set(''.join(input_lines))))
    length = len(input_lines[0])
    cons_matrix = {}

    for base in bases:
        cons_matrix[base] = []
        for pos in range(length):
            pos_count = 0
            for strand in input_lines:
                if base == strand[pos]:
                    pos_count += 1
            cons_matrix[base].append(str(pos_count))

    output = ""
    for pos in range(length):
        cons_base = ''
        max = -1
        for base in cons_matrix:
            if int(cons_matrix[base][pos]) > int(max):
                max = cons_matrix[base][pos]
                cons_base = base
        output += cons_base


    print(output)
    for key in cons_matrix:
        print(key + ':', ' '.join(cons_matrix[key]))



# best solution
def cons(strings):
    from collections import Counter
    counters = map(Counter, zip(*strings))
    consensus = "".join(c.most_common(1)[0][0] for c in counters)
    profile_matrix = "\n".join(b + ": " + \
        " ".join(str(c[b]) for c in counters) for b in "ACGT")
    return consensus + "\n" + profile_matrix
