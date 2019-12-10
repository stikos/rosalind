class Pair:
    def __init__(rabbit_pair, uid):
        rabbit_pair.age = 0
        rabbit_pair.uid = uid

if __name__ == "__main__":
    death, lf_exp = list(map(int, open('rosalind_fibd.txt', 'r').read().split()[:2]))
    
    pairs = []
    pairs.append(Pair(str(len(pairs))))
    for month in range(death):
        for pair in pairs:
            if pair.age == 0:
                pair.age += 1
            elif 1 <= pair.age < lf_exp:
                pairs.append(Pair(str(len(pairs))))
                pair.age += 1
            else: 
                pairs.append(Pair(str(len(pairs))))
                pairs.remove(pair)
            print(pair.uid + " Age:" + str(pair.age))

