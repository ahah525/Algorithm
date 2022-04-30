n = int(input())  # 창고 개수
graph = list(map(int, input().split()))  # n개의 식량 개수

d = [0] * 100
d[0] = graph[0]
d[1] = max(graph[0], graph[1])  # 둘 중 최댓값
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + graph[i])

print(d[n - 1])