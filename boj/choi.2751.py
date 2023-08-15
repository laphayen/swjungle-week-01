"""quick sort without additional list creation. check [boj/ex2750.py]
check also https://choiwheatley.notion.site/quick-sort-8720f36d603840f1b37fa73465c76eb0"""

from typing import MutableSequence, Callable
from random import randint

standard_input = "1000\n" + "".join(
    [str(randint(-1000, 1000)) + "\n" for _ in range(1000)]
)


def partition(ls: MutableSequence, lo: int, hi: int, less: Callable[[int, int], bool]):
    pivot_idx = randint(lo, hi - 1)
    # move pivot last of the element
    ls[pivot_idx], ls[hi - 1] = ls[hi - 1], ls[pivot_idx]
    pivot_idx = hi - 1

    count = 0  # count will be the separating point between less(x, pivot) and other
    for i in range(lo, pivot_idx):
        # iterate EXCEPT pivot
        if less(ls[i], ls[pivot_idx]):
            ls[i], ls[lo + count] = ls[lo + count], ls[i]
            count += 1
    # move pivot to the right place
    ls[pivot_idx], ls[lo + count] = ls[lo + count], ls[pivot_idx]
    return lo + count


def qsort(ls: MutableSequence, lo: int, hi: int, less: Callable[[int, int], bool]):
    """
    - lo: starting index (inclusive)
    - hi: end index (exclusive)
    - less: function that can customize ordering
    """
    if hi - lo <= 1:
        return
    pivot = partition(ls, lo, hi, less)
    qsort(ls, lo, pivot, less)
    qsort(ls, pivot + 1, hi, less)  # pivot은 넣으면 무한재귀


n = int(input())
ls = [int(input()) for _ in range(n)]
qsort(ls, 0, len(ls), lambda x, y: x < y)
{print(x) for x in ls}
