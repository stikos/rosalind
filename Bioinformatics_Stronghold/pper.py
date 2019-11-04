# my solution
from math import factorial, pow

if __name__ == '__main__':
    nums, subset = list(map(int, open('rosalind_pper.txt', 'r').read().split(" ")))

    res = factorial(nums) / factorial(nums - subset) 

    print(res % 1000000)
