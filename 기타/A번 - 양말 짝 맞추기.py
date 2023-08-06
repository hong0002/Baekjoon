# 양말
# $5$개가 주어집니다. 각 양말에는 숫자가 하나씩 쓰여있습니다. 같은 숫자가 쓰인 양말 두 개를 모으면 양말 한 쌍이 됩니다.
#
# 쌍을 만들 수 있는 양말을 두 개씩 두 쌍 빼면 남는 양말에 쓰인 숫자는 무엇인가요?
#
#
# 각 양말에 쓰인 숫자
# $5$개가 한 줄에 하나씩 주어집니다. 입력으로 주어지는 모든 숫자는
# $0$ 이상
# $9$ 이하입니다. 항상 양말을 두 개씩 두 쌍 만들 수 있는 입력만 주어집니다.
#
#
# 첫 줄에 남는 양말에 쓰인 숫자를 출력하세요.

from collections import Counter
import sys
input = sys.stdin.readline

nums = []
[nums.append(int(input())) for _ in range(5)]
c = Counter(nums)
for i, v in c.items():
    if v % 2 == 1:
        print(i)
