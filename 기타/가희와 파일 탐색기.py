# 가희는 jo_test 폴더에 들어와 있습니다. 가희는 jo_test에 있는 파일 N개를 아래 기준에 따라 정렬하려고 합니다.
#
# 파일명 (FILENAME) 사전순으로
# 파일명 (FILENAME)이 같다면 가희가 설치한 OS에서 인식하는 확장자가 붙은 것이 먼저 나오게
# 1과 2로도 순서를 결정할 수 없다면, 파일 확장자 (EXTENSION) 사전 순으로
# 파일 N개를 문제에서 설명하는 정렬 기준에 따라 정렬해 주세요. 사전순의 기준은 아스키 코드 순입니다.
#
#
# 첫 번째 줄에 jo_test 폴더에 있는 파일 개수 N과 가희가 설치한 OS에서 인식하는 파일 확장자의 개수 M이 공백으로 구분되어 주어집니다.
#
# 2번째 줄부터 N+1번째 줄까지 FILENAME.EXTENSION 형식의 문자열이 주어집니다. 여기서 .은 온점을 의미합니다.
#
# FILENAME은 소문자와 숫자로만, EXTENSION은 소문자로만 이루어져 있습니다.
#
# 그 다음 줄 부터 가희가 설치한 OS에서 인식하는 파일 확장자 (EXTENSION) M개가 주어집니다.
#
#
# 기준에 따라 정렬된 결과를 출력해 주세요.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
files = list()
ext = set()
[files.append(input().rstrip()) for _ in range(n)]
[ext.add(input().rstrip()) for _ in range(m)]

# 정렬
result = sorted(files, key=lambda x: (x[:x[:].find('.')], x.split('.')[1] not in ext, x[x[:].find('.')+1:])) # 2번째 조건에서 not in을 통해서 reverse
[print(i) for i in result]
