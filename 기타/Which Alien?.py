# 입력 받기
antenna_count = int(input())
eye_count = int(input())

# 우주에 알려진 외계인 종류와 조건에 따라 가능한 외계인 찾기
possible_aliens = []

# TroyMartian: at least 3 antenna and at most 4 eyes
if 3 <= antenna_count <= 4 and 0 <= eye_count <= 4:
    possible_aliens.append("TroyMartian")

# VladSaturnian: at most 6 antenna and at least 2 eyes
if 0 <= antenna_count <= 6 and 2 <= eye_count:
    possible_aliens.append("VladSaturnian")

# GraemeMercurian: at most 2 antenna and at most 3 eyes
if 0 <= antenna_count <= 2 and 0 <= eye_count <= 3:
    possible_aliens.append("GraemeMercurian")

# 결과 출력
for alien in possible_aliens:
    print(alien)
