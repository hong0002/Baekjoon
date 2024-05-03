# Read inputs
N = int(input())
S = input()
T = input()

# Initialize the Hamming distance counter
hamming_distance = 0

# Calculate the Hamming distance
for i in range(N):
    if S[i] != T[i]:
        hamming_distance += 1

# Output the result
print(hamming_distance)
