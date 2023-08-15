
# 이해x, 코드만 카피

n = int(input())

num_l = list(map(int, input().split()))

# 방문 확인
visited = [0] * n 

result = 0

def sol(arr):
    global answer
    if len(arr) == n:
        s = 0
        for i in range(n-1):
            s += abs(arr[i] - arr[i+1])
        result = max(result, s)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(num_l[i])
            sol[i]
            visited[i] = False
            arr.pop()
sol([])
print(result)