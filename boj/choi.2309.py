"""permutation을 직접 구현해보기"""
from itertools import permutations

MAXN = 9

ls = [int(input()) for _ in range(MAXN)]

for perm in permutations(ls, 7):
    if sum(perm) == 100:
        {print(x) for x in sorted(perm)}
        break
