standard_input = "2 3 1"

from enum import Enum, auto


class Cmp(Enum):
    Less = auto()
    Greater = auto()
    Equal = auto()


def compare(lhs, rhs) -> Cmp:
    if lhs < rhs:
        return Cmp.Less
    elif lhs > rhs:
        return Cmp.Greater
    return Cmp.Equal


def sol_recur(dim: int, r: int, c: int, lo: int, hi: int) -> int:
    if dim == 0:
        return lo
    # 넓이와 변의 길이를 저장한다.
    side = 2**dim
    area = side**2
    # 각 분면의 넓이와 변의 길이를 저장한다.
    cell_side = side // 2
    cell_area = cell_side**2

    match (compare(r, cell_side), compare(c, cell_side)):
        case (Cmp.Less, Cmp.Less):
            # 1분면에 있음
            hi = lo + cell_area
        case (Cmp.Less, Cmp.Greater | Cmp.Equal):
            # 2분면에 있음
            lo += cell_area
            hi = lo + cell_area
            c -= cell_side
        case (Cmp.Greater | Cmp.Equal, Cmp.Less):
            # 3분면에 있음
            lo += cell_area * 2
            hi = lo + cell_area
            r -= cell_side
        case _:
            # 4분면에 있음
            lo += cell_area * 3
            hi = lo + cell_area
            r -= cell_side
            c -= cell_side
    return sol_recur(dim - 1, r, c, lo, hi)


if __name__ == "__main__":
    n, r, c = [int(e) for e in input().split()]

    print(sol_recur(n, r, c, 0, 2 ** (2 * n)))
