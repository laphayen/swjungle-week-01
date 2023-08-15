"""도수정렬을 사용한 문제풀이
참고: https://www.acmicpc.net/source/58913744"""
from sys import stdin, stdout

standard_input = """10
5
2
3
1
4
2
3
5
1
7
"""

MAX_V = 10_000
num_list = [0 for _ in range(MAX_V + 1)]
n = int(input())

for line in stdin:
    num_list[int(line.strip())] += 1

for idx, cnt in enumerate(num_list):
    if cnt == 0:
        continue
    for _ in range(cnt):
        stdout.write(str(idx) + "\n")
