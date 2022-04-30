t = int(input())  # 테스트 케이스 수
for _ in range(t):
  n = int(input()) 
  # 피보나치 수 0, 1의 0, 1 호출 횟수 초기화
  zero = [1, 0] 
  one = [0, 1]

  if n > 1:
    for i in range(2, n + 1):  
      zero.append(zero[i - 1] + zero[i - 2])
      one.append(one[i - 1] + one[i - 2])
  print(zero[n], one[n])  # n번째 피보나치수 0, 1 호출 횟수

'''
def fibo(n):
  if n == 0:    
    return 0
  elif n == 1: 
    return 1
  else:
    # 기록된 값이 없으면 계산
    if d[n][0] == 0:  
      d[n][0] = fibo(n - 1) + fibo(n - 2)  # n번째 피보나치 수
      d[n][1] = d[n - 1][1] + d[n - 2][1]  # n번째 피보나치 수의 0 호출 횟수
      d[n][2] = d[n - 1][2] + d[n - 2][2]  # n번째 피보나치 수의 1 호출 횟수
    return d[n][0]

t = int(input())  # 테스트 케이스 수
for _ in range(t):
  n = int(input())  # 
  d = [[0, 0, 0] for _ in range(41)]  # 40이하의 자연수/0
  d[0] = [0, 1, 0]
  d[1] = [1, 0, 1]
  
  fibo(n)
  print(d[n][1], d[n][2])  # n번째 피보나치수 0, 1 호출 횟수
'''  