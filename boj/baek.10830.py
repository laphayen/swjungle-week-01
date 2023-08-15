

def mul(n, mat1, mat2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000
    return result

def devide(n, b, mat):
    if b == 1:
        return mat
    elif b == 2:
        return mul(n, mat, mat)
    else:
        tmp = devide(n, b//2, mat)
        if b % 2 == 0:
            return mul(n, tmp, tmp)
        else:
            return mul(n, mul(n, tmp, tmp), mat)


n, b = map(int, input().split())

mat = [list(map(int, input().split())) for i in range(n)]

result = devide(n, b, mat)

for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()