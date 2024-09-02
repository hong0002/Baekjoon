def format_number(n):
    # Convert the number to string to manipulate digits
    s = str(n)
    # Initialize a list to hold parts of the number
    parts = []
    # We start from the end and move backwards
    length = len(s)
    
    # Traverse the string in chunks of 3 from the end to the start
    for i in range(length, 0, -3):
        start = max(0, i - 3)  # Make sure start index is not negative
        part = s[start:i]      # Extract part of the string
        parts.append(part)     # Append to the list of parts
    
    # Since we collected parts from right to left, we need to reverse them
    formatted_number = ','.join(reversed(parts))
    return formatted_number

# Read input
n = int(input().strip())

# Output formatted number
print(format_number(n))
