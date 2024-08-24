def main():
    import sys
    input = sys.stdin.read
    
    # Read all input at once
    data = input().split('\n')
    
    # The first line is the word to search for
    search_word = data[0]
    
    # The rest is the text
    text_lines = data[1:]
    
    # Initialize count
    total_count = 0
    
    # Count occurrences in each line
    for line in text_lines:
        total_count += line.count(search_word)
    
    # Print the result
    print(total_count)

if __name__ == "__main__":
    main()
