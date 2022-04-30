n = int(input())  # 수열 크기
graph = list(map(int, input().split()))  # 크기가 n인 수열
d = [0] * n  # i번째까지 연속된 수의 합의 최댓값
d[0] = graph[0]

for i in range(1, n):
  d[i] = max(d[i - 1] + graph[i], graph[i])
print(max(d))
  



