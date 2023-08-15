standard_input = "100 99 1000000000"

from math import ceil

a, b, v = [int(x) for x in input().split(" ")]

print(ceil((v - a) / (a - b)) + 1)
