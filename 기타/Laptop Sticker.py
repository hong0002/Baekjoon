# Read input values from standard input
wc, hc, ws, hs = map(int, input().split())

# Calculate if the sticker fits with one cm spare on all sides
# The sticker needs at least 2 cm more on each dimension of the laptop (1 cm for each side)
if wc - ws >= 2 and hc - hs >= 2:
    print(1)  # It fits
else:
    print(0)  # It does not fit
