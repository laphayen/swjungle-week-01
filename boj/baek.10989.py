import sys

# 계수 정렬을 하기 위해 리스트 생성
li = [0 for _ in range(10001)]

# n을 입력을 받는다.
N = int(sys.stdin.readline())

# 인풋으로 받은 수가 몇변 들어왔는지 빈도 저장
for _ in range(N):
    num = int(sys.stdin.readline())
    # 바로 계수 정렬 인덱스에 접근하여 요소 위치에 +1
    li[num] += 1

# 배열의 시작부터 돌며 저장된 빈도만큼 인덱스값을 출력
for i in range(1, 10001):
    if li[i] != 0:
        for _ in range(li[i]):
            print(i)