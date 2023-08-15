standard_input = "734 893"

from collections import deque


def sol(a: str, b: str):
    for i in range(2, -1, -1):
        if a[i] < b[i]:
            return "".join(reversed(b))
        elif a[i] > b[i]:
            return "".join(reversed(a))


x, y = [x for x in input().split(" ")]
print(sol(x, y))
