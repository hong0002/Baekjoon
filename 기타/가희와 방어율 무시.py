def can_damage(monster_defense, user_ignore):
    user_effective_defense = monster_defense - (monster_defense * user_ignore / 100)
    return 1 if user_effective_defense < 100 else 0

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
result = can_damage(a, b)
print(result)
