n = int(input())

ans = 0
row = [0] * n


def is_promising(x):
    # 행을 돌면서 검사
    for i in range(x):
        # 열과 대각선 2개를 검한다.
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # 만약 같으면 실패 반환
            return False
    # 4방향 검사 후 없을 경우 성공 반환
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)