t = int(input())  # 테스트 케이스 수
d = [0] * 101
d[1:6] = [1, 1, 1, 2, 2]  # 1~5번째 값 초기화
for i in range(6, 101):
  d[i] = d[i - 1] + d[i - 5]

for _ in range(t):
  n = int(input())  # 1이상 100이하
  print(d[n])
