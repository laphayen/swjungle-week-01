
import sys

def dfs(start, now, cost):
    global result
    # 모든 도시를 돌았고 다시 원점으로 돌아온다면
    if start == now and all(visited):
        # 비용과 결과값 중 작은 값을 저장
        result = min(result, cost)
        return
    else:
        for next in range(n):
            # 다음 노드의 값이 0이거나 방문하지 않았을 경우
            if map[now][next] > 0 and not visited[next]:
                # 방문을 표시
                visited[next] = True
                # 다시 dfs 탐색
                dfs(start, next, cost+map[now][next])
                # 방문을 해제
                visited[next] = False

n = int(input())
map = [list(map(int, input().split())) for i in range(4)]
visited = [0]*n
result = sys.maxsize

dfs(0, 0, 0)

print(result)