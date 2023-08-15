from enum import Enum
from functools import total_ordering
from itertools import permutations
from typing import List

standard_input = """6
1 2 3 4 5 6
2 1 1 1
"""


@total_ordering
class Op(Enum):
    """참고: https://stackoverflow.com/a/39269589/21369350"""

    Add = 0
    Sub = 1
    Prd = 2
    Div = 3

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


MAPPER = [Op.Add, Op.Sub, Op.Prd, Op.Div]


def calc_one(x: int, y: int, operator: Op) -> int:
    if operator is Op.Div and y == 0:
        raise ZeroDivisionError
    match operator:
        case (Op.Add):
            return x + y
        case (Op.Sub):
            return x - y
        case (Op.Prd):
            return x * y
        case (Op.Div):
            if x < 0:
                # -1 // 3 => 0이 아니라 -1이 나와서 버그
                return -(abs(x) // y)
            return x // y


def calculate(num_ls: List[int], op_ls: List[Op]) -> int:
    result = num_ls[0]
    for idx, num in enumerate(num_ls[1:]):
        result = calc_one(result, num, op_ls[idx])
    return result


n = int(input())
num_ls = [int(x) for x in input().split()]
op_int_ls = [int(x) for x in input().split()]
op_ls = []
for id, amt in enumerate(op_int_ls):
    for _ in range(amt):
        op_ls.append(MAPPER[id])


sorted(op_ls)
_max = -1000000000
_min = 1000000000
for ops in permutations(op_ls):
    result = calculate(num_ls, list(ops))
    _max = max(_max, result)
    _min = min(_min, result)

print(_max)
print(_min)
