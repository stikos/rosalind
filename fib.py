# my solution
def fib(months, offsprings):
    if months > 2:
        return fib(months - 1, offsprings) + fib(months - 2, offsprings) * offsprings

    else:
        return 1

if __name__ == "__main__":
    print(fib(29, 5))

# best solution (timewise)
# non-recursive
def fib_non_recursive(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b



