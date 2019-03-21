# my solution
import urllib.request
import re

if __name__ == '__main__':
    input_lines = open('rosalind_mprt.txt', 'r').readlines()
    prot = re.compile(r'(?=(N[^P][S,T][^P]))')
    for prot_id in input_lines[:]:
        content = urllib.request.urlopen("https://www.uniprot.org/uniprot/" + prot_id.strip() + ".fasta").read().decode()
        content = content[content.find('\n'):].replace('\n', '')
        idxs = [pos.start()+1 for pos in prot.finditer(content)]
        if idxs:
            print(prot_id.strip())
            print(*idxs, sep=' ')
