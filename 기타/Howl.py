import sys

s = sys.stdin.readline().strip()
n = len(s)

# We will output a valid howl of length n+1:
# "AHO" + alternating 'W' and 'O' for (n-2) characters, starting with 'W'.
m = n - 2  # number of characters to append

sys.stdout.write("AHO")

pairs = m // 2
sys.stdout.write("WO" * pairs)
if m % 2 == 1:
    sys.stdout.write("W")

sys.stdout.write("\n")
