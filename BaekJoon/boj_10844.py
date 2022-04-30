n = int(input())  # 1이상 100이하 자연수
d = [[0] * 10 for _ in range(n)]
d[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
  for j in range(10):
    if j == 0:  d[i][j] = (d[i - 1][j + 1])
    elif j == 9:  d[i][j] = d[i - 1][j - 1]
    else:
      d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

print(sum(d[n - 1]) % 10**9)