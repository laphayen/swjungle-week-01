
n = int(input())
n_l = list(map(int, input().split()))
m = int(input())
m_l = list(map(int, input().split()))

n_l.sort()

for i in range(m):
    find = False
    target = m_l[i]
    s = 0
    e = n-1
    while s <= e:
        pc = int((s+e)/2)
        pc_value = n_l[pc]
        if pc_value > target:
            e = pc -1
        elif pc_value < target:
            s = pc + 1
        else:
            find = True
            break
    
    if find:
        print(1)
    else:
        print(0)