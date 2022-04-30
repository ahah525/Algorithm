'''
# 1. 피보나치 수열(단순 재귀)
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
'''
'''
# 2. 피보나치 수열(top-down)
d = [0] * 100  # 메모

def fibo(x):
  if x == 1 or x == 2:
    return 1
  # 기록된 값이면 바로 리턴
  if d[x] != 0:  return d[x]
  # 기록된 값이 아니면 계산후 리턴
  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]
'''
# 3. 피보나치 수열(bottom-up)
d = [0] * 100  # DP 테이블

d[1], d[2] = 1, 1  # 첫 번째, 두 번째 수는 1로 초기화
n = 99

# n번째 피보나치 수열 값 구하기
for i in range(3, n + 1):
  d[i] = d[i - 1] + d[i - 2]

print(d[n])