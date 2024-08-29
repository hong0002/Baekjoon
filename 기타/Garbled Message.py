import sys

def unscramble_message():
    # Reading from standard input until EOF
    garbled_text = sys.stdin.read()
    
    # Replace the garbled substring with the original substring
    unscrambled_text = garbled_text.replace("iiing", "th")
    
    # Output the unscrambled text
    print(unscrambled_text, end='')

if __name__ == "__main__":
    unscramble_message()
