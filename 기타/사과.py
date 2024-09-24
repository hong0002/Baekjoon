# Read number of schools
N = int(input())

total_leftover = 0

# Read each school's data
for _ in range(N):
    students, apples = map(int, input().split())
    
    # Calculate leftover apples
    leftover_apples = apples % students
    total_leftover += leftover_apples

# Print the total leftover apples
print(total_leftover)
