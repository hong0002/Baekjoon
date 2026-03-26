m = int(input())
n = int(input())

rotate = {
    '0': '0',
    '1': '1',
    '8': '8',
    '6': '9',
    '9': '6'
}

def is_rotatable(num):
    s = str(num)
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] not in rotate:
            return False
        if rotate[s[left]] != s[right]:
            return False
        left += 1
        right -= 1

    return True

count = 0
for num in range(m, n + 1):
    if is_rotatable(num):
        count += 1

print(count)
