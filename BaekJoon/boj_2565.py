import sys
input = sys.stdin.readline

n = int(input())  # 전깃줄 개수
graph = [list(map(int, input().split())) for _ in range(n)]
graph.sort()  # 첫번쨰 

d = [1] * n  # i번째 전깃줄이 마지막인 모든 전깃줄이 교차하지 않게하는 최대 전깃줄의 개수
for i in range(1, n):
  for j in range(i):
    if graph[j][1] < graph[i][1]:
      d[i] = max(d[i], d[j] + 1)
print(n - max(d))  # 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수
