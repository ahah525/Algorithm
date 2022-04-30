n, l = map(int, input().split())  # 과일 개수, 초기 길이
h = list(map(int, input().split()))  # 과일 높이(n개)
h.sort()  # 과일높이 오름차순 정렬
length = l  # 스네이크버드 길이(초기 길이로 초기화)

for i in range(n):
  # 과일 높이가 스네이크 버드 길이보다 작거나 같으면
  if(h[i] <= length):
    # 과일 먹기
    length += 1  # 스네이크 버드 길이 1 증가
    n -= 1       # 과일 개수 1 감소
  else:
    break

print(length)