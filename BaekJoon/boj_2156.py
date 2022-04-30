import sys
input = sys.stdin.readline

n = int(input())  # 포도주 잔의 개수(1이상 10000이하)
graph = [int(input()) for _ in range(n)]  # n개의 포도주 양

if n == 1:
  print(graph[0])
else:
  d = [0] * n  # i번째까지 마실 수 있는 포도주의 최대양
  d[0] = graph[0]
  d[1] = graph[0] + graph[1]
  for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + graph[i], d[i - 3] + graph[i-1] + graph[i])
  print(d[n - 1])