from math import sqrt

count = int(input())
nums = list(map(int, input().split()))
for n in nums:
    if (n == 1):
        count -= 1
        continue
    for i in range(2, int(sqrt(n))+1):
        if(n == i):
            continue
        if(n%i == 0):
            count -= 1
            break
print(count)