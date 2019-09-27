# my solution
from fasta_in import get_input
from collections import defaultdict

if __name__ == "__main__":
    input_lines = get_input("rosalind_long.txt")

    reads = defaultdict()

    for sub_s in input_lines:
        try:
            match_pos = input_lines.index(*[x for x in input_lines if sub_s[len(sub_s)//2 - 2 :] in x and x != sub_s])
        
        except Exception:
            reads[sub_s] = {'n' : None}
            continue
        if sub_s not in reads:
            reads[sub_s] = {}
        if input_lines[match_pos] not in reads:
            reads[input_lines[match_pos]] = {}

        reads[sub_s]['n'] = input_lines[match_pos]
        reads[input_lines[match_pos]]['p'] = sub_s

    start = None
    for key, val in reads.items():
        if val['n'] != None and 'p' not in val:
            start = key
            break
    
    output = start
    curr = start
    while True:
        str1 = curr
        str2 = reads[curr]['n']
        char_count = len(str2)//2
        while(str1.find(str2[: char_count]) >= 0):
            char_count += 1
        output += str2[char_count-1 :]
        curr = str2
        if reads[curr]['n'] is None:
            break

    print(output)

