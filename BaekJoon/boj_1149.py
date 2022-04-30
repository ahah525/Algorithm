import sys
input = sys.stdin.readline

n = int(input())  # 집 수
# n개의 집 칠하는 비용(R, G, B)
d = [list(map(int, input().split())) for _ in range(n)]

# 1행부터 집 칠하는 최소 비용 계산
for i in range(1, n):
  # 현재칸과 다른 열들의 값 중 최소값 선택
  d[i][0] += min(d[i - 1][1], d[i - 1][2])
  d[i][1] += min(d[i - 1][0], d[i - 1][2])
  d[i][2] += min(d[i - 1][0], d[i - 1][1])

for i in d:
  print(i)
print(min(d[n - 1]))  # 모든 집을 칠하는 최소 비용
'''
import sys
input = sys.stdin.readline

n = int(input())  # 집 수
# n개의 집 칠하는 비용(R, G, B)
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * 3 for _ in range(n)] # i번째 집까지 칠하는 최소 비용

for i in range(n):
  # 초기화
  if i == 0:
    for j in range(3):
      d[i][j] = graph[i][j]
  else:
    for j in range(3):
      d[i][j] = graph[i][j] + min(d[i - 1][(j + 1) % 3],  d[i - 1][(j + 2) % 3])

print(min(d[n - 1]))  # 모든 집을 칠하는 최소 비용
'''
