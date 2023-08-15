"""
8*8 체스판에 8개의 퀸을 두는 모든 경우의 수에서 시작하여 주어진 조건에 따라 가능성을 하나씩 줄여 나가는 작업을 수행해보자.
"""

from typing import List


SIDE = 8
total = 0
pos = [0 for _ in range(SIDE)]  # 각 열에 배치한 퀸의 위치, pos[col] = row
row_visited = [False for _ in range(SIDE)]

# f(row, col) = ne_visited[row + col]
ne_visited = [False for _ in range(SIDE * 2 - 1)]

# f(row, col) = se_visited[row - col + SIDE - 1]
se_visited = [False for _ in range(SIDE * 2 - 1)]


def print_queens(pos: List[int]):
    global total
    # print([(row, col) for col, row in enumerate(pos)])
    total += 1


def sol_recur(col: int):
    global pos
    if col == SIDE:
        print_queens(pos)
        return
    for row in range(SIDE):
        ne_idx = row + col
        se_idx = col - row + SIDE - 1
        if row_visited[row] or ne_visited[ne_idx] or se_visited[se_idx]:
            continue
        # let's visit this row!!
        row_visited[row] = True
        ne_visited[ne_idx] = True
        se_visited[se_idx] = True
        pos[col] = row

        sol_recur(col + 1)

        # undo visit
        row_visited[row] = False
        ne_visited[ne_idx] = False
        se_visited[se_idx] = False


sol_recur(0)
print(f"total count: {total}")
