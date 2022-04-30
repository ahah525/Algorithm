import sys
input = sys.stdin.readline

n = int(input())  # 계단의 개수(300이하 자연수)
graph = [int(input()) for _ in range(n)]  # n개의 계단 점수

if n == 1:
  print(graph[0])
else:
  d = [0] * 300
  d[0] = graph[0]
  d[1] = graph[0] + graph[1]
  for i in range(2, n):
    d[i] = graph[i] + max(d[i - 3] + graph[i - 1], d[i - 2])
  print(d[n - 1])
