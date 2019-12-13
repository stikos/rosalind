# my solution

if __name__ == '__main__':
    edges = open('rosalind_tree.txt', 'r').read().split("\n")
    num = int(edges[0])
    edges = list(map(str.split, edges[1:]))
    nodes = list(map(str, range(num+1)))[1:]
    count = 0

    check_overall = []
    for check_point in nodes:
        check_set = [check_point]

        if check_point not in check_overall:
            while check_set:
                for node in check_set:
                    temp_edges = [x for x in edges if node in x]
                    new_nodes = list(set([y for x in temp_edges for y in x if y != node and y not in check_overall]))
                    check_set.extend(new_nodes)
                    check_set = list(set(check_set))
                    check_set.remove(node)
                    check_overall.append(node)
            count += 1

    print(count - 1)

# best solution
# N-1-M, where N is the number of nodes and M the number of edges...