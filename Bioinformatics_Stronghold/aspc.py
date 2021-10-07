from math import factorial

n, m = 1943, 1216

res = 0
for k in range(m, n+1):
    # integer division; I don't need to spend bits for a float and I'll need as many as I can get
    res = res + (factorial(n)//(factorial(k)*factorial(n-k)))  

print(res%1000000)