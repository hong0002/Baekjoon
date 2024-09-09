def can_be_used_on_sign(word):
    valid_letters = {'I', 'O', 'S', 'H', 'Z', 'X', 'N'}
    for letter in word:
        if letter not in valid_letters:
            return "NO"
    return "YES"

# Read the input word
word = input().strip()

# Determine if the word can be used on the sign
result = can_be_used_on_sign(word)

# Output the result
print(result)
