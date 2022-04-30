from collections import deque

# BFS
def bfs(x, cnt):
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  queue.append((x, cnt))
  visited[x] = 1
  
  while queue:
    x, cnt = queue.popleft()
    visited[x] = 1

    # 끝 값에 도달하면
    if(x == k):
      return cnt
      
    for nx in [2 * x, x - 1, x + 1]:
      if(0 <= nx <= 100000):
        # 방문한적이 없으면
        if(visited[nx] == 0):
          if(nx == 2 * x):
            queue.append((nx, cnt))            
          else:
            queue.append((nx, cnt + 1))

n, k = map(int, input().split())  # 시작 위치, 끝 위치
visited = [0] * 100001
print(bfs(n, 0))


'''
from collections import deque

# BFS
def bfs(x, cnt):
  min_time = 1e9	# 최소 시간
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  queue.append((x, cnt))
  visited[x] = 1
  
  while queue:
    x, cnt = queue.popleft()
    visited[x] = 1

    # 끝 값에 도달하면
    if(x == k):
      # 처음 발견하면
      if(cnt < min_time):
        min_time = cnt
      
    dx = [x - 1, x + 1, 2 * x]
    for i in range(3):
      nx = dx[i]
      if(0 <= nx <= 100000):
        # 방문한적이 없으면
        if(visited[nx] == 0):
          if(i == 2):
            queue.append((nx, cnt))            
          else:
            queue.append((nx, cnt + 1))
  return min_time

n, k = map(int, input().split())  # 시작 위치, 끝 위치
visited = [0] * 100001
print(bfs(n, 0))
'''

