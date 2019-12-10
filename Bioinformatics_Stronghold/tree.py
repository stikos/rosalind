# my solution

if __name__ == '__main__':
    edges = open('rosalind_tree.txt', 'r').read().split("\n")[1:]
    edges = list(map(str.split, edges))
    groups = [edges.pop(0)]
    for i in edges:
        flag = False
        for cluster in groups:
            if any(x in cluster for x in i):
                print(i, cluster)
                cluster = list(set(cluster.extend(i)))
                i = True
        if not flag:
            groups.append(i)

    print(groups)

