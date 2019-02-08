# my solution
if __name__ == '__main__':
	in_str = ''.join(sorted("AGCTTTTCATTCTGACTG"))
	curr = in_str[0]
	index = 1
	prev_index = 0
	while index <= len(in_str)-1:
		if in_str[index] == curr and index != len(in_str)-1:
			index += 1

		elif index == len(in_str)-1:
			print(index - prev_index + 1)
			break

		else:
			curr = in_str[index]
			print(index - prev_index)
			prev_index = index

# best solution
print(*map("AGCTTTTCATTCTGACTG".count, "ACGT"))

		

