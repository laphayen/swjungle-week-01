standard_input = "999"

from itertools import islice
from collections import deque
from functools import reduce


def sliding_window(seq, n=2):
    """참고: https://stackoverflow.com/a/6822773
    참고: https://docs.python.org/3/library/itertools.html#itertools-recipes"""
    it = iter(seq)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def is_hansu(n: int) -> bool:
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return reduce(lambda x, y: x == y, [x - y for x, y in sliding_window(digits, 2)])


MAX = 1000
hansu = [0 for _ in range(MAX + 1)]
hansu[0] = 0

for i in range(100):
    # 두 자리수까지는 전부 한수
    hansu[i] = i

for i in range(100, MAX + 1):
    if is_hansu(i):
        hansu[i] = hansu[i - 1] + 1
    else:
        hansu[i] = hansu[i - 1]

print(hansu[int(input())])
