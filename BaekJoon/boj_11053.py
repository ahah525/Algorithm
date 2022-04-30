n = int(input())  # 수열의 길이(1이상 1000이하)
graph = list(map(int, input().split()))  # 수열
d = [1] * n  # graph[i]를 마지막 원소로 갖는 최장 부분 수열 길이
for i in range(1, n):
  # i보다 작은 원소들에 대해 
  for j in range(i):
    if graph[j] < graph[i]:    
      # 현재값 & graph[j]를 마지막에서 2번째 원소로 가졌을 때 최장 부분 수열의 길이 를 비교하여 최댓값 갱신 
      d[i] = max(d[i], d[j] + 1)
print(max(d))  # 최장 증가 부분 수열의 길이