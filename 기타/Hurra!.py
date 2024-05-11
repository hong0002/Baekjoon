def special_counting(N):
    for i in range(1, N + 1):
        if i % 77 == 0:
            print("Wiwat!")
        elif i % 7 == 0:
            print("Hurra!")
        elif i % 11 == 0:
            print("Super!")
        else:
            print(i)

# Read the input integer N from standard input
import sys
input = sys.stdin.read
N = int(input().strip())

# Call the function to perform the special counting
special_counting(N)
