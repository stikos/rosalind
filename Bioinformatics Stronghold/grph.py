# my solution
if __name__ == '__main__':
    input_lines = open('rosalind_grph.txt', 'r').read().splitlines()

    strands = {}
    curr = ""
    for line in input_lines:
        if line.startswith('>'):
            curr = line[1:]
            strands[curr] = ""

        else:
            strands[curr] += line

    graph = []
    for strand in strands:
        curr = strands[strand]
        for check in strands:
            if check != strand:
                if curr[-3:] == strands[check][:3]:
                    graph.append(strand + ' ' + check)

    print('\n'.join(graph))


# best solution
# less iterations over the data (mine is O(V^2))