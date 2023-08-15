"""quadtree"""
g_cnt = [0, 0]


def r_sol(side: int, r, c) -> None:
    if side == 1:
        # 한 칸밖에 남지 않음
        g_cnt[paper[r][c]] += 1
        return

    flatten = [x for row in range(r, r + side) for x in paper[row][c : c + side]]

    if all(x == flatten[0] for x in flatten):
        # side X side 칸이 모두 한 가지 색일 경우
        # 잘라낼 수 있는 색종이임
        g_cnt[paper[r][c]] += 1
        return
    # messy square, divide four times
    next_side = side // 2
    r_sol(next_side, r, c)  # 좌상단
    r_sol(next_side, r + next_side, c)  # 좌하단
    r_sol(next_side, r, c + next_side)  # 우상단
    r_sol(next_side, r + next_side, c + next_side)  # 우하단


n = int(input())
paper = [[int(x) for x in input().split()] for _ in range(n)]

r_sol(n, 0, 0)

print(g_cnt[0])
print(g_cnt[1])
