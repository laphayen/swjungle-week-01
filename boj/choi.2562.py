index = [i for i in range(1, 10)]
ls = [int(input()) for _ in range(9)]
ls_index = zip(ls, index)
ls_index = sorted(ls_index, key=lambda tup: tup[0])
print(ls_index[-1][0])
print(ls_index[-1][1])
