#my solution
import itertools

if __name__ == '__main__':
    nums, string = open('rosalind_lgis.txt', 'r').read().split('\n')[0:2]
    nums = int(nums)
    string = list(map(int, string.split()))

    lookup_t_a = {}
    lookup_t_d = {}

    for element in string:
        for idx in range(string.index(element) + 1, len(string)):         
            subseq_asc = [element]
            subseq_des = [element]
            for comp in string[idx:]:
                if not any(comp < x for x in subseq_asc):
                    subseq_asc.append(comp)
                elif not any(comp > x for x in subseq_des):
                    subseq_des.append(comp)
            if element in lookup_t_a:
                if len(lookup_t_a[element]) < len(subseq_asc):
                    lookup_t_a[element] = subseq_asc
            else:
                lookup_t_a[element] = [subseq_asc]
            if element in lookup_t_d:
                if len(lookup_t_d[element]) < len(subseq_des):
                    lookup_t_d[element] = subseq_des
            else:
                lookup_t_d[element] = [subseq_des]


    print(max(lookup_t_a.values(), key=len), sep=' ')
    print(max(lookup_t_d.values(), key=len), sep=' ')


