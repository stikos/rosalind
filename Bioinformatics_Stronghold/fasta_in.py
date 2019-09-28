import re

def get_input(filename):
    """
    Get FASTA formatted input
    """
    input_lines = re.split(r'>Rosalind_[0-9]+\n', open(filename, 'r').read())
    return [x.replace('\n', '') for x in input_lines[1:]]
