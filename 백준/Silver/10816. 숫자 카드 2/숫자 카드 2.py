N = int(input())
cards = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

check = dict() 
for card in cards: 
    if card in check:
        check[card] += 1 
    else:
        check[card] = 1

for target in targets:
    if target in check: 
        print(check[target], end=' ')
    else:
        print(0, end=' ')