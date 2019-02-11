# my solution
if __name__ == '__main__':
    input_lines = open('rosalind_subs.txt', 'r').readlines()
    idx = 0
    output = ""

    while idx != -1:
        pos = input_lines[0].strip('\n').find(input_lines[1].strip('\n'), idx)
        if pos != -1:
            idx = pos + 1
            output += " " + str(pos + 1)
        else:
            idx = -1

    print(output)



# best solution (so close)
dnaSeq = "GATATATGCATATACTT"
subSeq = "ATAT"

r = 0
while r != -1 :
        r = dnaSeq.find(subSeq,r+1)
        print(r+1)



