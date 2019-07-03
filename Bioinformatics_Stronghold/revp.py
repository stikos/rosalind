# my solution


def rev_cmp(orgnl_str):
    return orgnl_str.translate(orgnl_str.maketrans("ACGT", "TGCA"))[::-1]


if __name__ == "__main__":
    input_str = ''.join(open('rosalind_revp.txt', 'r').readlines()[1:]).replace('\n', '')
    for length in range(4, 13):
        for pos in range(len(input_str)):
            if pos <= len(input_str):
                check_str = input_str[pos: pos + length]
                if check_str == rev_cmp(check_str):
                    print(pos+1, length)