# 입력 받기
N = int(input())  # 친구들의 수
friend_tracks = input().split()  # 친구들의 트랙 정보 리스트
hello_bit_track = input()  # 헬로빗이 지원하는 트랙 정보

# 일치하는 트랙의 친구 수 계산
matching_friends = friend_tracks.count(hello_bit_track)

# 결과 출력
print(matching_friends)
