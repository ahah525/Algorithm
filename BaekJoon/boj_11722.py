import sys
input = sys.stdin.readline

n = int(input())  # 수열 크기(1이상 1000이하 자연수)
graph = list(map(int, input().split()))  # 크기 n인 수열
d = [1] * n
for i in range(1, n):
  for j in range(i):
    # i번째 값보다 큰 수에서 최댓값 갱신
    if graph[j] > graph[i]:
      d[i] = max(d[i], d[j] + 1)
print(max(d))
