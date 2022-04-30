n = int(input())  # 수열 크기(1이상 1000이하)
graph1 = list(map(int, input().split()))  # 수열 
graph2 = list(reversed(graph1))  # 역순으로 뒤집은 수열
d1 = [1] * n  # 가장 긴 증가하는 부분 수열
d2 = [1] * n  # 가장 긴 감소하는 부분 수열

# 최장 증가 부분 수열 & 최장 감소 부분 수열의 길이 구하기
for i in range(1, n):
  for j in range(i):
    if graph1[j] < graph1[i]:
      d1[i] = max(d1[i], d1[j] + 1)
    if graph2[j] < graph2[i]:
      d2[i] = max(d2[i], d2[j] + 1)
# 최장 증가 부분 수열 & 최장 감소 부분 수열의 길이 합의 최댓값
res = 0
for i in range(n):
  res = max(res, d1[i] + d2[n - 1 - i] - 1)
print(res)