"""modular exponentiation 참고: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-exponentiation"""
from math import ceil, log2


def modular_exponentiation(b: int, exp: int, m: int):
    """나머지 지수승 연산을 수행하는 알고리즘.
    $$
    b^{exp} \mod m
    $$
    """
    x = 1
    power = b % m
    k = ceil(log2(exp)) + 1

    for i in range(k):
        if (exp >> i) & 1 == 1:
            # a_i = 1 then,
            x = (x * power) % m
        power = (power * power) % m
    return x


b, exp, m = [int(x) for x in input().split()]

print(modular_exponentiation(b, exp, m))
