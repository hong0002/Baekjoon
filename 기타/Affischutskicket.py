# 함수를 정의합니다.
def calculate_weight(envelope_weight, poster_weight, leaflet_weight):
    # 종이의 면적을 계산합니다.
    envelope_area = 229 / 1000 * 324 / 1000 * 2  # C4 envelope area in m^2
    poster_area = 297 / 1000 * 420 / 1000 * 2    # A3 poster area in m^2
    leaflet_area = 210 / 1000 * 297 / 1000       # A4 leaflet area in m^2
    
    # 종이의 무게를 계산합니다.
    envelope_total_weight = envelope_weight * envelope_area
    poster_total_weight = poster_weight * poster_area
    leaflet_total_weight = leaflet_weight * leaflet_area
    
    # 전체 무게를 계산합니다.
    total_weight = envelope_total_weight + poster_total_weight + leaflet_total_weight
    
    return total_weight

# 입력을 받습니다.
envelope_weight, poster_weight, leaflet_weight = map(int, input().split())

# 함수를 호출하여 결과를 계산하고 출력합니다.
result = calculate_weight(envelope_weight, poster_weight, leaflet_weight)
print(round(result, 6))  # 소수점 이하 6자리까지 반올림하여 출력합니다.
