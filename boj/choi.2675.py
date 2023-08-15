t = int(input())

for _ in range(t):
    ls = [x for x in input().split(" ")]
    r = int(ls[0])
    s = ls[1]
    for c in s:
        for _ in range(r):
            print(c, end="")
    print()
