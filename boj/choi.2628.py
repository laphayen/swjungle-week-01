standard_input = """10 8
3
0 3
1 4
0 2
"""

# [0][n]: 가로로 자르는 점선, n번
# [1][m]: 세로로 자르는 점선, m번
cut_lines = [
    [
        0,
    ],
    [
        0,
    ],
]

row, col = [int(x) for x in input().split()]
cut_lines[0].append(col)
cut_lines[1].append(row)

num = int(input())

for _ in range(num):
    rowcol, pos = [int(x) for x in input().split()]
    cut_lines[rowcol].append(pos)

# sort

for lines in cut_lines:
    lines.sort()

max_hori = 0
max_vert = 0

for i in range(len(cut_lines[0]) - 1):
    max_hori = max(max_hori, cut_lines[0][i + 1] - cut_lines[0][i])

for i in range(len(cut_lines[1]) - 1):
    max_vert = max(max_vert, cut_lines[1][i + 1] - cut_lines[1][i])


print(max_hori * max_vert)
