
# 나무 자르기

def binary_search(li, srt, end):
    re = 0
    while srt <= end:
        mid = (srt+end) // 2
        total = 0

        for i in li:
            if i > mid:
                total += (i - mid)
        if total < m:
            end = mid-1
        else:
            re = mid
            srt = mid + 1
    return re


n, m = map(int, input().split())

tree_list = list(map(int, input().split()))

result = binary_search(tree_list, 0, max(tree_list))

print(result)