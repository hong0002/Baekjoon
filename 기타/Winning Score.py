# Apples scoring
apples_3_points = int(input())
apples_2_points = int(input())
apples_1_point = int(input())

# Bananas scoring
bananas_3_points = int(input())
bananas_2_points = int(input())
bananas_1_point = int(input())

# Calculate total points for each team
apples_total_points = apples_3_points * 3 + apples_2_points * 2 + apples_1_point
bananas_total_points = bananas_3_points * 3 + bananas_2_points * 2 + bananas_1_point

# Determine the winner or if it's a tie
if apples_total_points > bananas_total_points:
    print('A')
elif apples_total_points < bananas_total_points:
    print('B')
else:
    print('T')
