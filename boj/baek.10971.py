
# 이해x

import sys

def dfs(start, now, value, cnt):
    global result
    if cnt == n:
        if l[now][start]:
            value += l[now][start]
            if result > value:
                result = value
        return

    if value > result:
        return
    
    for i in range(n):
        if not visited[i] and l[now][i]:
            visited[i] = 1
            dfs(start, i, value + l[now][i], cnt +1)
            visited[i] = 0

n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]

result = sys.maxsize

visited = [0] * n

for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(result)