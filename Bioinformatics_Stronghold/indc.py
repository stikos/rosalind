from math import log10

n = 5

res = []
for i in range(2*n):
    res.append(log10(pow(1/2, i)))

print(res)