# 입력값을 받아옵니다.
num_test_cases = int(input())

# 각 테스트 케이스에 대해 반복합니다.
for _ in range(num_test_cases):
    lt, wt, le, we = map(int, input().split())

    # TelecomParisTech 운동장 면적
    telecom_area = lt * wt

    # Eurecom 운동장 면적
    eurecom_area = le * we

    # 결과 출력
    if telecom_area > eurecom_area:
        print("TelecomParisTech")
    elif eurecom_area > telecom_area:
        print("Eurecom")
    else:
        print("Tie")
