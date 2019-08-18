from itertools import permutations
if __name__ == "__main__":
    input_lines = open("rosalind_lexf.txt", "r").read()
    alpha, length = input_lines.split("\n")[:-1]
    alpha = alpha.replace(" ", "")
    # output = list(map(lambda x: x[0]+x[1], permutations(alpha, int(length))))
    # for char in alpha:
    #     output.append(char+char)
    # print(*sorted(output), sep="\n")

    def make_word(alpha, max_len, curr_len, word):
        if curr_len >= max_len:
            print(word)
            return
        else:
            for letter in alpha:
                make_word(alpha, max_len, curr_len + 1, word + letter)


    for char in alpha:
        make_word(alpha, int(length), 0, char)
