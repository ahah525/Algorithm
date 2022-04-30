n, m = map(int, input().split())

if(n == 1):
  res = 1
elif(n == 2):
  # 2, 3, 방향으로 밖에 못 움직임(m값과 상관없이 최대값은 4)
  res = min(4, (m + 1) // 2)
else:
  # 1, 2, 3, 4 방향 다 가능
  if(m <= 3):
    res = m
  else:
    if(m <= 6):
      res = min(4, m) 
    else:
      res = m -2
print(res)