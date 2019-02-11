# my solution
if __name__ == '__main__':
    input_lines = open('rosalind_gc.txt', 'r').readlines()
    data = {}
    line_id = ""
    for line in input_lines:
        line = line.strip("\n")
        if '>' in line:
            data[line] = ""
            line_id = line
        else:
            data[line_id] += line

    max_id = ""
    max_val = 0

    for line in data:
        temp = (data[line].count('G') + data[line].count('C')) / len(data[line])

        if temp > max_val:
            max_val = temp
            max_id = line

    print(max_id[1:], "\n", max_val * 100)


# best solution
# -