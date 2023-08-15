"""
가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 가능한 변의 길이 나열하기

==> 사실 약수 구하는 문제임
"""
from random import randint
from math import sqrt, ceil

area = randint(4, 12812)

for i in range(1, ceil(sqrt(area)) + 1):
    if area % i:
        continue
    print(f"{i} * {area // i} = {area}")
