# Reading input
algosia_scores = list(map(int, input().split()))
bajtek_scores = list(map(int, input().split()))

# Function to count occurrences of each score from 0 to 10
def score_count(scores):
    count = [0] * 11  # counts for scores 0 through 10
    for score in scores:
        count[score] += 1
    return count

# Compute the total score for Algosia and Bajtek
algosia_total = sum(algosia_scores)
bajtek_total = sum(bajtek_scores)

# Compare the total scores first
if algosia_total > bajtek_total:
    print("Algosia")
elif bajtek_total > algosia_total:
    print("Bajtek")
else:
    # If total scores are equal, compare the counts of each score from 10 to 0
    algosia_counts = score_count(algosia_scores)
    bajtek_counts = score_count(bajtek_scores)
    
    for i in range(10, -1, -1):  # Compare counts of scores from 10 down to 0
        if algosia_counts[i] > bajtek_counts[i]:
            print("Algosia")
            break
        elif bajtek_counts[i] > algosia_counts[i]:
            print("Bajtek")
            break
    else:
        # If still tied after comparing all scores, print "remis"
        print("remis")
