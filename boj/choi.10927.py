"""
외판원 순회 2
"""

standard_input = """4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
"""
Bitset = int  # 어차피 최대 N이 10이므로 정수형 하나에 때려넣자.

INF = 10_000_000

MAXN = 10
N = int(input())
W = [[int(x) if x != "0" else INF for x in input().split()] for _ in range(N)]

g_minimum = INF


def all(visited: Bitset, n: int) -> bool:
    """처음 n개의 비트가 전부 True일 경우에만 True"""
    mask = (1 << n) - 1
    return (mask & visited) == mask


def rsolve(cur: int, start: int, total: int, visited: Bitset) -> None:
    global g_minimum

    if all(visited, N):
        # start로 돌아갈 일만 남음.
        total += W[cur][start]
        g_minimum = min(g_minimum, total)
        return

    for i in range(N):
        if visited & (1 << i) or cur == i:
            # if visited[i] == True 와 동일함
            continue
        ### visited를 True -> recursion -> False로 하지 않는 이유는
        ### 해당 값을 전역적으로(또는 레퍼런스로) 관리하지 않고 독립적인 단일 변수로
        ### 관리하고 있기 때문입니다.
        # visited |= 1 << i  # register
        rsolve(i, start, total + W[cur][i], visited | 1 << i)
        # visited ^= 1 << i  # unregister


### visited에 1을 주고 시작하는 이유는 start에 바로 방문하지 않기 위함입니다.
### 어차피 종료조건을 통과하면 cur -> start 거리를 더해줄 것이기 때문에 방문체크를
### 할 필요가 없습니다.
rsolve(cur=0, start=0, total=0, visited=0b0001)
print(g_minimum)
