standard_input = """6
1 2 3 4 5 6
2 1 1 1
"""


n = int(input())
num_ls = [int(x) for x in input().split()]
addition_cnt, subtraction_cnt, product_cnt, division_cnt = [
    int(x) for x in input().split()
]


def r_sol(idx, total, on_leaf):
    """idx가 0이 아니라 1부터 시작하고 total이 ls[0]부터 시작한다는 점 참고"""
    global addition_cnt, subtraction_cnt, product_cnt, division_cnt, num_ls

    if idx == len(num_ls):
        on_leaf(total)
        return

    if addition_cnt:
        addition_cnt -= 1
        r_sol(idx + 1, total + num_ls[idx], on_leaf)
        addition_cnt += 1
    if subtraction_cnt:
        subtraction_cnt -= 1
        r_sol(idx + 1, total - num_ls[idx], on_leaf)
        subtraction_cnt += 1
    if product_cnt:
        product_cnt -= 1
        r_sol(idx + 1, total * num_ls[idx], on_leaf)
        product_cnt += 1
    if division_cnt:
        if total < 0:
            total = -(abs(total) // num_ls[idx])
        else:
            total //= num_ls[idx]
        division_cnt -= 1
        r_sol(idx + 1, total, on_leaf)
        division_cnt += 1


maximum = -1000000000
minimum = 1000000000


def on_leaf(total):
    global maximum
    global minimum
    maximum = max(maximum, total)
    minimum = min(minimum, total)


r_sol(1, num_ls[0], on_leaf)

print(maximum)
print(minimum)
