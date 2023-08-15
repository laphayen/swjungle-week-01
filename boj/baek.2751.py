# 오름차순 정렬
import sys
import heapq

def heapsort(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, value)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

import sys
n = int(input())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

li = heapsort(li)
for i in li:
     print(i)