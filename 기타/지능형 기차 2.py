def max_people_on_train(stops):
    max_people = 0
    current_people = 0

    for out_count, in_count in stops:
        current_people -= out_count
        current_people += in_count
        if current_people > max_people:
            max_people = current_people
    
    return max_people

# 입력 받기
stops = []
for _ in range(10):
    out_count, in_count = map(int, input().split())
    stops.append((out_count, in_count))

# 결과 출력
print(max_people_on_train(stops))
