x, y, w, h = [int(i) for i in input().split(" ")]

print(min([x, y, h - y, w - x]))
