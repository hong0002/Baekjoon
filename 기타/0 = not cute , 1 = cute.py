# Read the number of participants
N = int(input().strip())

# Initialize counts
cute_count = 0

# Read each vote and count the number of 1's (cute votes)
for _ in range(N):
    vote = int(input().strip())
    if vote == 1:
        cute_count += 1

# Check if the number of cute votes is greater than half of the total votes
if cute_count > N // 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
