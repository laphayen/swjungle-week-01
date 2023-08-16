def div_con(start_r, start_c, size):
    global cnt
    if size == 2:
        if start_r == r and start_c == c: # 2사분면
            print(cnt)
            return
        cnt += 1
        if start_r == r and start_c + 1 == c: # 1사분면
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c == c: # 3사분면
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c + 1 == c: # 4사분면
            print(cnt)
            return
        cnt += 1
    else:
        size //= 2
        div_con(start_r, start_c, size) # 2사분면
        div_con(start_r, start_c + size, size) # 1사분면
        div_con(start_r + size, start_c, size) # 3사분면
        div_con(start_r + size, start_c + size, size) # 4사분면

N, r, c = map(int, input().split())
cnt = 0

div_con(0, 0, 2 ** N)