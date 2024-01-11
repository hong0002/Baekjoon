def detect_typing_method(s):
    if s == "fdsajkl;" or s == "jkl;fdsa":
        return "in-out"
    elif s == "asdf;lkj" or s == ";lkjasdf":
        return "out-in"
    elif s == "asdfjkl;":
        return "stairs"
    elif s == ";lkjfdsa":
        return "reverse"
    else:
        return "molu"

# 입력 받기
input_str = input()

# 결과 출력
result = detect_typing_method(input_str)
print(result)
