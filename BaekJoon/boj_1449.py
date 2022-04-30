n, l = map(int, input().split())  # 새는 곳 수, 테이프 길이
loc = list(map(int, input().split()))  # 새는 곳 위치
loc.sort() # 올림차순 정렬

cnt = 1  # 테이프 수
tape_end = loc[0] + l  # 최근 테이프 끝 지점 갱신
for i in range(1, n):
  # 최근 테이프 끝 지점이 현재 위치의 끝 지점보다 작거나 같으면
  if(loc[i] + 1 > tape_end):
    # 새로운 테이프 붙이기
    tape_end = loc[i] + l  # 테이프 끝 지점 갱신
    cnt += 1  # 테이프 개수 증가

print(cnt)