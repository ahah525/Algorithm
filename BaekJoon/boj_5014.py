from collections import deque
 
# BFS
def bfs(x):
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  queue.append((x, 0))
  visited[x] = 1  
  
  while queue:
    x, cnt = queue.popleft()
    # 목표 층수에 도달하면 종료
    if(x == g):
      return cnt
    # 위, 아래 탐색
    for i in range(2):
      nx = x + dx[i]
      # 층수가 범위 내이고 방문하지 않은 층이면
      if(1 <= nx <= f):
        if(visited[nx] == 0):
          # 삽입, 방문처리
          queue.append((nx, cnt + 1))
          visited[nx] = 1
  return "use the stairs"
 
#f: 총 층수, g: 목표 층수, s: 현재 층수, u: 위로 이동가능 층수, d: 아래로 이동가능 층수
f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)  # 방문 여부
dx = [u, -d]  # 위, 아래 탐색 방향
 
print(bfs(s))

'''
from collections import deque

# BFS
def bfs(x):
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  queue.append((x, 0))
  visited = {x}
  
  while queue:
    x, cnt = queue.popleft()
    # 목표 층수에 도달하면 종료
    if(x == g):
      return cnt
    # 위, 아래 탐색
    for i in range(2):
      nx = x + dx[i]
      # 층수가 범위 내이고 방문하지 않은 층이면
      if(1 <= nx <= f and nx not in visited):
        # 삽입, 방문처리
        queue.append((nx, cnt + 1))
        visited.add(nx)
  return "use the stairs"

#f: 총 층수, g: 목표 층수, s: 현재 층수, u: 위로 이동가능 층수, d: 아래로 이동가능 층수
f, s, g, u, d = map(int, input().split())
dx = [u, -d]  # 위, 아래 탐색 방향

print(bfs(s))
'''
