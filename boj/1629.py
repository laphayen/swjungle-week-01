import sys
a,b,c = map(int,sys.stdin.readline().split())

def multi (a,n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n//2)
        # 짝수인 경우
        if n % 2 ==0:
            return (tmp * tmp) % c
        # 홀수 인 경우 
        else:
            return (tmp  * tmp * a) % c
          
print(multi(a,b))