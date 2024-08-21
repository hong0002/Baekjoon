def count_parity_errors(data_line):
    errors = 0
    # Process each 8-bit chunk
    for i in range(0, len(data_line), 8):
        chunk = data_line[i:i+8]
        # Get the first 7 bits and the 8th bit
        data_bits = chunk[:7]
        parity_bit = chunk[7]
        # Count the number of 1's in the first 7 bits
        count_ones = data_bits.count('1')
        # Determine the expected parity bit
        expected_parity = '1' if count_ones % 2 != 0 else '0'
        # Compare with the given parity bit
        if expected_parity != parity_bit:
            errors += 1
    return errors

# Read the number of lines
n = int(input().strip())

# Process each line and output the result
for _ in range(n):
    data_line = input().strip()
    print(count_parity_errors(data_line))
