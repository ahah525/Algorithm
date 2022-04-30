n = int(input())  # 설탕 무게
arr=[]	# 경우의 수

x = 0
while True:
  y = (n - 3  * x) / 5
  # 탈출 조건
  if(y < 0):
    break
  # 정수이면
  if(y == int(y)):
    arr.append(x + int(y))
  x += 1  

# 경우의 수가 없는 경우
if(len(arr) == 0):
  print(-1)
else:
  print(min(arr))	# 최소값 출력


'''
n = int(input())  # 설탕 무게
res = 0  # 봉지 수

while n >= 0:
  # 5의 배수이면
  if(n % 5 == 0):
    res += n // 5  # 봉지 수 추가
    print(res)  
    break
  n -= 3  # 5의 배수가 될 때까지 반복
  res += 1  # 봉지 수 추가
# while 문이 False이면(n이 음수가 되면)
else:
  print(-1)

'''