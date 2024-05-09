def count_socks_pairs(socks):
    count_B = socks.count('B')
    count_C = socks.count('C')
    
    pairs_B = count_B // 2
    pairs_C = count_C // 2
    
    return pairs_B + pairs_C

# Input reading (for example usage, replace this with actual input mechanism if required)
socks = input().strip()

# Calculate and print the result
print(count_socks_pairs(socks))
