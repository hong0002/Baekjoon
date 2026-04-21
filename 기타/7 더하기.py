digit_to_code = {
    '0': '063',
    '1': '010',
    '2': '093',
    '3': '079',
    '4': '106',
    '5': '103',
    '6': '119',
    '7': '011',
    '8': '127',
    '9': '107'
}

code_to_digit = {v: k for k, v in digit_to_code.items()}


def decode(code_str):
    result = ''

    for i in range(0, len(code_str), 3):
        code = code_str[i:i + 3]
        result += code_to_digit[code]

    return int(result)


def encode(num):
    result = ''

    for ch in str(num):
        result += digit_to_code[ch]

    return result


while True:
    line = input().strip()

    if line == "BYE":
        break

    left, right = line.split('+')
    right = right[:-1]

    a = decode(left)
    b = decode(right)

    c = a + b
    encoded_c = encode(c)

    print(f"{left}+{right}={encoded_c}")
