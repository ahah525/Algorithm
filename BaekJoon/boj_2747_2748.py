n = int(input())  # 45이하 자연수
d = [0] * (n + 1)
d[0], d[1] = 0, 1
for i in range(2, n + 1) :
  d[i] = (d[i - 1] + d[i - 2])
print(d[n])
'''
def fibo(x):
  if x == 0:  return 0
  if x == 1:  return 1
  # 기록되지 않았으면 계산
  if d[x] == 0:  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

n = int(input())  # 90이하 자연수
d = [0] * (n + 1)
d[0], d[1] = 0, 1
fibo(n)
print(d[n])  # n번째 피보나치수
'''