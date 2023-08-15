from functools import reduce


s = str(reduce(lambda a, b: a * b, [int(input()) for _ in range(3)]))
result = [0 for _ in range(10)]
for c in s:
    result[int(c)] += 1

for c in result:
    print(c)
