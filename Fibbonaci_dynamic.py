counted = {0: 1, 1: 1}


def count_fib(n: int):
    for num in range(0, n + 1):
        cached_result = counted.get(n)
        if cached_result:
            return cached_result
        counted[n] = count_fib(n-1) + count_fib(n-2)
        return counted[n]

print(count_fib(10))