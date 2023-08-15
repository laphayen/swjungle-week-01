from typing import List


def sol(ls: List[int]) -> float:
    avg = sum(ls) / len(ls)
    num = len([x for x in ls if x > avg])
    return (num / len(ls)) * 100


c = int(input())
for _ in range(c):
    ls = [int(x) for x in input().split(" ")]
    n = ls[0]
    print(f"{sol(ls[1:]):.3f}%")
