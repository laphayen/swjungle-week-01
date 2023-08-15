standard_input = "20"

from typing import List, Tuple


def find_other_pile(x: int, y: int) -> int:
    return x ^ y


def hanoi(num: int, x: int, y: int) -> int:
    """x 기둥에 박혀있는 원반 num개를 y 기둥으로 모두 옮기는 경우의 수"""
    if num == 1:
        return 1
    z = find_other_pile(x, y)
    return hanoi(num - 1, x, z) + hanoi(1, x, y) + hanoi(num - 1, z, y)


def hanoi_with_inst(num: int, x: int, y: int, ls: List[Tuple[int, int]]) -> int:
    if num == 1:
        ls.append((x, y))
        return 1
    z = find_other_pile(x, y)
    steps = [
        hanoi_with_inst(num - 1, x, z, ls),
        hanoi_with_inst(1, x, y, ls),
        hanoi_with_inst(num - 1, z, y, ls),
    ]
    return sum(steps)


def solve(n):
    if n <= 20:
        ls = []
        print(hanoi_with_inst(n, 1, 3, ls))
        {print(x, y) for x, y in ls}
    else:
        print(2**n - 1)


solve(int(input()))
