def haxor_speak(s):
    # Create translation table using str.maketrans
    translation_table = str.maketrans({
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5'
    })
    
    # Translate the string using the translation table
    return s.translate(translation_table)

# Read input
input_string = input().strip()

# Get the haxor version of the input
haxor_version = haxor_speak(input_string)

# Output the transformed string
print(haxor_version)
