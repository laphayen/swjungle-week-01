
# 이해x, 코드만 카피

n = int(input())

num_l = list(map(int, input().split()))

# 방문 확인
visited = [0] * n 

result = 0

def sol(arr):
    # 내가 찾고자 하는 조건이 맞을 때
    global answer
    if len(arr) == n:
        s = 0
        for i in range(n-1):
            s += abs(arr[i] - arr[i+1])
        result = max(result, s)
        return
    
    # 조건이 맞지 않을 경우 - 하나씩 넣고 빼면서 확인하는 과정
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(num_l[i])
            sol[i]
            visited[i] = False
            arr.pop()

# 깊이는 0부터 시작
sol([])
print(result)