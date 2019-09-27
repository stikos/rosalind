from fasta_in import get_input
complements = {'A' : 'T', 'G' : 'C', 'C' : 'G', 'T' : 'A'}

def check_reads(read1, read2):
	comp_read2 = ''.join([complements[x] for x in read2][::-1])
	comp_count = 0	
	h_count = 0
	for i, j, k in zip(read1, read2, comp_read2):
		if i != j:			
			h_count += 1
		if i != k:
			comp_count += 1
		if h_count > 1 and comp_count > 1:
			return None
	return read2

if __name__ == '__main__':

	input_lines = get_input('rosalind_corr.txt')

	#remove correct reads
	corr_list = []
	for read in input_lines:
		if input_lines.count(read) >= 2 or ''.join([complements[x] for x in read][::-1]) in input_lines:
			corr_list.append(read)
	
	corr_list = list(set(corr_list))

	input_lines = [x for x in input_lines if x not in corr_list]
	matched = []
	for read in input_lines:
		for check in corr_list:
			if read not in matched:
				if check != read:
					res = check_reads(read, check)
					if res is not None:
						print(read+"->"+res)
						matched.append(read)
