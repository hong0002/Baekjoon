G, S, C = map(int, input().split())
P = 3*G + 2*S + C

# best victory card
victory = None
if P >= 8:
    victory = "Province"
elif P >= 5:
    victory = "Duchy"
elif P >= 2:
    victory = "Estate"

# best treasure card
if P >= 6:
    treasure = "Gold"
elif P >= 3:
    treasure = "Silver"
else:
    treasure = "Copper"

if victory is None:
    print(treasure)
else:
    print(f"{victory} or {treasure}")
