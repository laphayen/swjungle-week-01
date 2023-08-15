"""완전탐색 + set 버전"""
standard_input = """4
2
1
2
12
1
"""

from typing import Set


string = str()
visited = [False for _ in range(10)]
cards = []
possibilities = set()


def sol_recur(remain: int):
    global string
    global visited
    if remain == 0:
        possibilities.add(string)
        return

    for idx, card in enumerate(cards):
        if visited[idx]:
            continue
        # draw a card!
        length = len(string)
        visited[idx] = True
        string += str(card)

        sol_recur(remain - 1)

        # undraw a card!
        visited[idx] = False
        string = string[:length]


n = int(input())
k = int(input())
for _ in range(n):
    cards.append(int(input()))

sol_recur(k)
print(len(possibilities))
