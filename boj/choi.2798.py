from itertools import permutations

standard_input = """5 21
5 6 7 8 9
"""

n, m = [int(x) for x in input().split()]
ls = [int(x) for x in input().split() if int(x) < m]
print(max([sum(perm) for perm in permutations(ls, 3) if sum(perm) <= m]))
