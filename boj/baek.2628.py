
w, h = map(int, input().split())

# 최대 넓이, 높이 설정
w_l = [0, w]
h_l = [0, h]

cut = int(input())

# 자르는 횟수만큼 반복
for i in range(cut):
    # 자를는 좌표를 입력 받는다.
    where, value = map(int, input().split())
    if where == 1:
        w_l.append(value)
    else:
        h_l.append(value)

# 입력 받은 값들을 정령 후
w_l.sort()
h_l.sort()

# 종이를 자른 후에 최대 넓이는 가장 긴 가로와 세로를 곱한 값이다.
# 따라서 for문을 통해 w_l, h_l에서 가장 긴 구간을 구해서 곱한다.

# 가장 긴 구간을 저장
max_w, max_h = 0, 0

# 가장 긴 가로
# (len(w_l))이면 w_l[i+1]은 리스트 인덱스 밖의 값이다.
for i in range(len(w_l)-1):
    if max_w < (w_l[i+1] - w_l[i]):
        max_w = (w_l[i+1] - w_l[i])

# 가장 긴 세로
# (len(h_l))이면 h_l[i+1]은 리스트 인덱스 밖의 값이다.
for i in range(len(h_l)-1):
    if max_h < (h_l[i+1] - h_l[i]):
        max_h = (h_l[i+1] - h_l[i])

print(max_h*max_w)