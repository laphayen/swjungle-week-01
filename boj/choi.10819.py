from collections import deque
from itertools import permutations, islice


def sliding_window(seq, n):
    it = iter(seq)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for each in it:
        window.append(each)
        yield tuple(window)


n = int(input())
ls = [int(x) for x in input().split()]
print(
    max(
        [
            sum([abs(x - y) for x, y in sliding_window(perm, 2)])
            for perm in permutations(sorted(ls))
        ]
    )
)
