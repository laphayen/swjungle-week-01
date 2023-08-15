short_man = [int(input()) for i in range(9)]

# 난쟁이들의 키의 임시 저장 공간
tmp = []

def dfs(depth, start):
    if depth == 7:
        if sum(tmp) == 100:
            for i in sorted(tmp):
                print(i)
            exit()
        else:
            return
    
    for i in range(start, len(short_man)):
        # 난쟁이 1명 추가
        tmp.append(short_man[i])
        # dfs 탐색 - 다음 인덱스를 탐색할 수 있도록 깊이와 인덱스를 더해준다.
        dfs(depth+1, i+1)
        # 합이 100명이 아닌 경우 난쟁이를 꺼낸다.
        tmp.pop()

dfs(0, 0)