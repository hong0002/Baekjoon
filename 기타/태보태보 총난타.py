s = input().strip()
face = "(^0^)"
idx = s.find(face)

left = s[:idx]
right = s[idx + len(face):]

print(left.count('@'), right.count('@'))
