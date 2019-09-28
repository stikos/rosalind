# my solution
from itertools import permutations, combinations
if __name__ == '__main__':
    num = int(input())
    perms = []

    for order in permutations(list(range(num+1))[1:], num):
        perms.append(order)

    final = perms[:]

    for order in perms:
        for i in list(range(len(order)+1))[1:]:
            candidates = list(combinations(order, i))
            for tup in candidates:
                temp = []
                for element in order:
                    if element not in tup:
                        temp.append(element)
                    else:
                        temp.append(element*-1)
                final.append(temp)

    with open('out.txt', 'w') as out:
        out.write(str(len(final)) + '\n')
        for i in final:
            out.write(' '.join(map(str, i)) + '\n')


# best solution
# create +/- pairs of the range, then return the cartesian product of the unpacked tuples !!!!
from itertools import permutations, product

def signedPermutations(n):
    for perm in permutations(range(1, n + 1)):
        for signed_perm in product(*[(-element, element) for element in perm]):
            yield signed_perm