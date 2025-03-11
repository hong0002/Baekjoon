bowl = input()
height = 10
for i, v in enumerate(bowl):
    if i == 0:
        after = v
        continue
    if v == after:
        height += 5
    else:
        height += 10
    after = v
print(height)
