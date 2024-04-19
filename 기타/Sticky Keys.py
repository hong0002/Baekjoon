def correct_message(message):
    corrected_message = ""
    prev_char = ""
    
    for char in message:
        if char != prev_char:
            corrected_message += char
        prev_char = char
    
    return corrected_message

# Input
message = input()

# Output corrected message
print(correct_message(message))
