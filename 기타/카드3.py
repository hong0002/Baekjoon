n = int(input().strip())
cards = list(map(int, input().split()))
result = sum(cards) - max(cards)
print(result)
