# my solution
import re
def get_all_substrings(input_string):
    length = len(input_string)
    return set([input_string[i:j + 1] for i in range(length) for j in range(i,length)])


if __name__ == '__main__':
    input_lines = re.split(r'>Rosalind_[0-9]+\n', open('rosalind_lcsm.txt', 'r').read())
    input_lines = [x.replace('\n', '') for x in input_lines[1:]]
    subs = None
    for x in input_lines:
        temp_subs = get_all_substrings(x)
        if not subs:
            subs = temp_subs
        else:
            subs = subs & temp_subs

    print(max(list(subs), key=len))

# best solution
# sort them in ascending length order, the lcs cannot be longer than our shortest string!