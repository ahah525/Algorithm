t = int(input())  # 테스트 케이스 수
for _ in range(t):
  n = int(input())  # 정수
  d = [0] * 11  # 11보다 작은 양수
  d[1], d[2], d[3] = 1, 2, 4 
  for i in range(4, n + 1):
    # 마지막에 더해진 값이 1, 2, 3인 경우
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

  print(d[n])