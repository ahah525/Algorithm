import sys

r, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
route = ""  # 경로
# r: 홀수, c: 짝수 / r: 홀수, c: 홀수
if(r % 2 != 0):
  route = ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1)
# r: 짝수, c: 홀수
elif(r % 2 == 0 and c % 2 != 0):
  route = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1)
# r: 짝수, c: 짝수
elif(r % 2 == 0 and c % 2 == 0):
  min = 1000  # 최솟값
  min_x = -1
  min_y = -1
  # 최소값 위치 찾기
  for i in range(r):
    for j in range(c):
      # 짝수행에 대하여 
      if((i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0)):
        if(min > arr[i][j]):
          min = arr[i][j]
          min_x = i
          min_y = j
  # 1. 빈 칸 이전 열에 대한 경로(DRUR)
  route += ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (min_y // 2)
  #route += " "    
  # 2. 빈 칸을 둘러싼 경로
  y1 = (min_y // 2) * 2      # 첫번째 열
  y2 = (min_y // 2) * 2 + 1  # 두번째 열
  x = 0    # 2번 경로 시작 행
  y = y1   # 2번 경로 시작 열
  
  while True:
    # 마지막 행, 두번째 열이면 탈출
    if(x == r - 1 and y == y2):
      break
    # 현재 첫번째 열이고 오른쪽 칸이 빈칸이 아니면 오른쪽으로
    if(y == y1 and [x, y2] != [min_x, min_y]):
      route += 'R'
      y += 1
    # 현재 두번째 열이고 왼쪽 칸이 빈칸이 아니면 왼쪽으로
    elif(y == y2 and [x, y1] != [min_x, min_y]):
      route += 'L'
      y -= 1
    # 마지막 행이 아니면 아래로
    if(x != r - 1):
      route += 'D'
      x += 1
      
  '''
  if(min_y % 2 == 0):
    target_route = 'RDLD' * (r // 2 - 1) + 'R'
    route += target_route[0 : 4 * (min_x - 1) + 1] + 'D' + target_route[4 * (min_x - 1) + 1 : len(target_route)]  
  # 빈 칸을 둘러싼 경로(y가 홀수, x가 0이 아니면)
  elif(min_y % 2 != 0 and min_x != 0):
    target_route = 'RDLD' * (r // 2 - 1) + 'R'
    route += target_route[0 : 2 * min_x] + 'D' + target_route[2 * min_x: len(target_route)]     
  # 빈 칸을 둘러싼 경로(y가 홀수, x가 0이면)
  elif(min_y % 2 != 0 and min_x == 0):
    target_route = 'DRDL' * (r // 2 - 1) + 'DR'
    route += target_route
  '''
  #route += " "   
  # 3. 빈 칸 이후 열에 대한 경로(RURD)
  route += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - min_y - 1) // 2)
  
print(route)