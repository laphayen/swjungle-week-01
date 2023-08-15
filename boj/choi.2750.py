"""quick sort"""

from typing import List
from random import randint

standard_input = "1000\n" + "".join(
    [str(randint(-1000, 1000)) + "\n" for _ in range(1000)]
)


def qsort(ls: List[int]) -> List[int]:
    if len(ls) <= 1:
        return ls
    pivot_idx = randint(0, len(ls) - 1)
    pivot = ls.pop(pivot_idx)
    left = [x for x in ls if x <= pivot]
    right = [x for x in ls if x > pivot]

    return qsort(left) + [pivot] + qsort(right)


n = int(input())
ls = [int(input()) for _ in range(n)]
{print(x) for x in qsort(ls)}
