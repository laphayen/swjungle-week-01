standard_input = """6
1 2 3 4 5 6
2 1 1 1
"""


def r_sol(
    idx,
    total,
    addition_cnt,
    subtraction_cnt,
    product_cnt,
    division_cnt,
    on_leaf,
    num_ls,
):
    """idx가 0이 아니라 1부터 시작하고 total이 ls[0]부터 시작한다는 점 참고"""
    if idx == len(num_ls):
        on_leaf(total)
        return
    if addition_cnt:
        r_sol(
            idx + 1,
            total + num_ls[idx],
            addition_cnt - 1,
            subtraction_cnt,
            product_cnt,
            division_cnt,
            on_leaf,
            num_ls,
        )
    if subtraction_cnt:
        r_sol(
            idx + 1,
            total - num_ls[idx],
            addition_cnt,
            subtraction_cnt - 1,
            product_cnt,
            division_cnt,
            on_leaf,
            num_ls,
        )
    if product_cnt:
        r_sol(
            idx + 1,
            total * num_ls[idx],
            addition_cnt,
            subtraction_cnt,
            product_cnt - 1,
            division_cnt,
            on_leaf,
            num_ls,
        )
    if division_cnt:
        if total < 0:
            total = -(abs(total) // num_ls[idx])
        else:
            total //= num_ls[idx]
        r_sol(
            idx + 1,
            total,
            addition_cnt,
            subtraction_cnt,
            product_cnt,
            division_cnt - 1,
            on_leaf,
            num_ls,
        )


n = int(input())
num_ls = [int(x) for x in input().split()]
addition_cnt, subtraction_cnt, product_cnt, division_cnt = [
    int(x) for x in input().split()
]

maximum = -1000000000
minimum = 1000000000


def on_leaf(total):
    global maximum
    global minimum
    maximum = max(maximum, total)
    minimum = min(minimum, total)


r_sol(
    1,
    num_ls[0],
    addition_cnt,
    subtraction_cnt,
    product_cnt,
    division_cnt,
    on_leaf,
    num_ls,
)

print(maximum)
print(minimum)
