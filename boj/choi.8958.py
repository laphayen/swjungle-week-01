def sol(s: str):
    acc = 0
    score = 0

    for c in s:
        if c == "O":
            acc += 1
            score += acc
        else:
            acc = 0

    return score


n = int(input())

for _ in range(n):
    print(sol(input()))
