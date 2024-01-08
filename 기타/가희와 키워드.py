# 가희는 블로그를 운영하고 있습니다. 가희는 블로그에 글을 쓰기 위해, 메모장에 키워드를 적곤 합니다.
#
# 지금까지 메모장에 써진 키워드는 모두 서로 다르며, 총 N개가 존재합니다.
#
# 가희는 새로운 글을 작성할 때, 최대 10개의 키워드에 대해서 글을 작성합니다.
#
# 이 키워드들 중에 메모장에 있었던 키워드는 가희가 글을 쓴 이후, 메모장에서 지워지게 됩니다.
#
# 가희는 블로그에 글을 쓰고 나서, 메모장에 있는 키워드 개수가 몇 개인지 알고 싶습니다. 가희를 도와주세요.
#
#
# 첫 번째 줄에 가희가 메모장에 적은 키워드 개수 N, 가희가 블로그에 쓴 글의 개수 M이 공백으로 구분해서 주어집니다.
#
# 2번째 줄부터 N+1번째 줄까지 메모장에 적은 키워드 N개가 주어집니다.
#
# N+2번째 줄부터 N+M+1번째 줄까지, 가희가 쓴 글과 관련된 키워드가 , (쉼표)로 구분해서 주어집니다. 공백으로 구분되지 않음을 유의해 주세요.
#
#
# x번째 줄에는 x번째 글을 쓰고 난 후에 메모장에 남아 있는 키워드의 개수를 출력해 주세요.

import sys
input = sys.stdin.readline

class Note:
    def __init__(self, data):
        self.note = set()
        [self.note.add(input().rstrip()) for i in range(data)] # 키워드 입력

    def write_text(self):
        text = list(input().rstrip().split(","))
        for word in text:
            if word in self.note: self.note.remove(word) # 키워드를 사용하면 제거
                
        print(len(self.note))

n, m = map(int, input().split())
note = Note(n)
[note.write_text() for _ in range(m)]
