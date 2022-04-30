n = int(input())  # 사람 수
times = list(map(int, input().split()))  # 각 사람의 인출 시간
res = 0  # 총 최소 시간
times.sort()  # 오름차순 정렬

for i in range(n):
  # 0 ~ i까지 더하기
  for j in range(i+1):
    res += times[j]
print(res)
