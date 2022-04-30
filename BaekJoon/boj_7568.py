import sys
input = sys.stdin.readline
 
n = int(input())  # 사람 수
# n 명의 몸무게, 키
graph = [list(map(int, input().split())) for _ in range(n)]
rank = []  # 덩치 등수
 
for i in range(n):
  cnt = 0  # 자신보다 큰 덩치의 사람수
  for j in range(n):
    # 자기 자신이 아니면 비교
    if i != j:
      # 자신보다 키, 몸무게 둘 다 크면
      if graph[i][0] < graph[j][0] and graph[i][1] < graph[j][1]:
        cnt += 1
  rank.append(cnt + 1)
print(*rank)