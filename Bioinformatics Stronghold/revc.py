# my solution
if __name__ == '__main__':
	complements = {'A' : 'T', 'G' : 'C', 'C' : 'G', 'T' : 'A'} 
	print("".join(map(lambda x: complements[x], "AAAACCCGGT"[::-1])))
	
# cool solution
print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))