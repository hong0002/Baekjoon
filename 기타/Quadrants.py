x, y = map(float, input().split())
while (x, y) != (0, 0):
    if x == 0.0 or y == 0.0: print("AXIS")
    elif x > 0.0 and y > 0.0: print("Q1")
    elif x < 0.0 < y: print("Q2")
    elif x < 0.0 and y < 0.0: print("Q3")
    else: print("Q4")
    x, y = map(float, input().split())
print("AXIS")
