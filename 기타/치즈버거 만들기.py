# 승현이가 일하는 햄버거 가게에는 요리 재료로 사용할 햄버거 패티가
# $A$개, 슬라이스 치즈가
# $B$개 있다. 치즈버거를 만들기 위해서는 패티와 치즈를 각각 한 개 이상 고른 후 햄버거 빵 사이에 패티와 치즈를 번갈아 쌓아야 한다. 단, 패티의 개수는 치즈의 개수보다 정확히 한 개 더 많이 골라야 한다.
#
# 승현이는 가게에 있는 요리 재료를 가지고 최대한 큰 치즈버거를 하나 만들려고 한다. 치즈버거의 크기는 패티와 치즈의 개수를 더한 것과 같다. 승현이가 만들 수 있는 치즈버거의 최대 크기를 구해보자.
#
#
# 첫째 줄에 패티의 개수
# $A(2\leq A\leq 100)$와 치즈의 개수
# $B(1\leq B\leq 100)$가 공백으로 구분되어 주어진다.
#
#
# 승현이가 만들 수 있는 치즈버거의 최대 크기를 출력한다.

a, b = map(int, input().split())
print(b + b + 1) if a > b else print(a+a-1)
