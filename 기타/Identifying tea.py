# Input reading
tea_type = int(input())
answers = list(map(int, input().split()))

# Count the number of correct guesses
correct_guesses = answers.count(tea_type)

# Output the result
print(correct_guesses)
