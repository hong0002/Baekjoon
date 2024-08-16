# Reading the six lines from input
line1 = input().strip()
line2 = input().strip()
line3 = input().strip()
line4 = input().strip()
line5 = input().strip()
line6 = input().strip()

# Calculating the number of characters in each line
x1 = len(line1)
x2 = len(line2)
x3 = len(line3)
x4 = len(line4)
x5 = len(line5)
x6 = len(line6)

# Outputting the results in the specified format
print(f"Latitude {x1}:{x2}:{x3}")
print(f"Longitude {x4}:{x5}:{x6}")
