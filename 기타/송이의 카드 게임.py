N, K = map(int, input().split())

cards = []

for person in range(1, N + 1):
    nums = list(map(int, input().split()))
    for num in nums:
        cards.append((person, num))

idx = 0

while len(cards) > 1:
    owner, x = cards.pop(idx)

    if len(cards) == 0:
        break

    idx = (idx + x - 1) % len(cards)

winner, last_card = cards[0]
print(winner, last_card)
