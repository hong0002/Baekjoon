def beauty_of_number(k):
    k_str = str(k).rstrip('0')  # Remove trailing zeros
    beauty = k_str.count('0')   # Count the remaining zeros
    return beauty

if __name__ == "__main__":
    k = int(input())
    result = beauty_of_number(k)
    print(result)
