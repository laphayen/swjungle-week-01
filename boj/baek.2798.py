def combination(deck, idx, cards):
    global max_s
    if len(cards) == 3:
        s = sum(cards)
        if s <= m and s > max_s:
            max_s = s
    else:
        for i in range(idx, len(deck)):
            cards.append(deck[i])
            combination(deck, i+1, cards)
            cards.pop()

n, m = map(int, input().split())
deck = list(map(int, input().split()))
 
max_s = 0
combination(deck, 0, [])
print(max_s)