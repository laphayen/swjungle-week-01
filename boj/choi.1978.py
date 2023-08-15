standard_input = """4
1 3 5 7"""

from math import sqrt

seive = [True for _ in range(1002)]
seive[0] = False
seive[1] = False

for i in range(2, int(sqrt(1000)) + 1):
    if seive[i]:
        for times in range(2, 1000 // i + 1):
            seive[i * times] = False

n = input()
print(len([x for x in input().split() if seive[int(x)]]))
