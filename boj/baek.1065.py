
n = int(input())

def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        # 각 자릿수 별로 분해
        l = list(map(int, str(i)))
        # 1~9는 0과 1 사이의 1의 등차 수열
        # 0과 2는 0과 2사이의 등차 수열
        # 11~99 는 1과 1사이의 0
        # 27은 2과 7사이의 5 등차수열
        if i < 100:
            cnt += 1
        # 100 부터는 백의 자리와 십의 자리 차이가
        # 십의 자리와 일의 자의 차이가 같아야 등차 수열이다.
        elif l[0] - l[1] == l[1] - l[2]:
            cnt += 1
    return cnt

print(hansu(n))
