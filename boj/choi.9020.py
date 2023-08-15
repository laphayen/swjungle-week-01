standard_input = """3
8
18
16
"""
from typing import Tuple
from math import sqrt
from bisect import bisect_left

MAX = 10_000
seive = [True for _ in range(MAX + 2)]
seive[0] = False
seive[1] = False

for i in range(2, int(sqrt(MAX)) + 1):
    if seive[i]:
        for times in range(2, MAX // i + 1):
            seive[i * times] = False

# from seive, find all prime numbers

primes = [index for index, value in enumerate(seive) if value]


def get_goldbach_partition(n: int) -> Tuple[int, int]:
    for x in range(n // 2, 1, -1):
        # x 보다 작거나 같은 가장 큰 소수
        prime1 = primes[bisect_left(primes, x)]
        prime2 = n - prime1
        if seive[prime2]:
            return (prime1, prime2) if prime1 < prime2 else (prime2, prime1)
    return (0, 0)


t = int(input())
for _ in range(t):
    a, b = get_goldbach_partition(int(input()))
    print(a, b)
