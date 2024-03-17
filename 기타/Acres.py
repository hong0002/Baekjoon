def bags_of_corn(field_width, field_length):
    # Convert field dimensions to acres
    field_area_acres = (field_width * field_length) / 4840
    
    # Calculate the number of bags needed
    bags_needed = field_area_acres / 5
    
    # Round up to the nearest integer
    bags_needed = int(bags_needed) + (bags_needed % 1 > 0)
    
    return bags_needed

# 입력 받기
field_width, field_length = map(int, input().split())

# 결과 출력
print(bags_of_corn(field_width, field_length))
