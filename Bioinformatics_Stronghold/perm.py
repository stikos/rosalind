# my solution
from itertools import permutations

x = int(open("rosalind_perm.txt",'r').read().strip())
num_list = list(range(1, x+1))
output = list(permutations(num_list))
print(len(output))
print(*[str(x)[1:-1].replace(',', '') for x in output], sep='\n')
