from collections import deque
import sys
input = sys.stdin.readline

# BFS
def bfs(start, end):
  queue = deque()
  # 시작점 4방향으로 삽입, 방문처리
  for i in range(4):
    queue.append((start[0], start[1], i))
    visited[start[0]][start[1]][i] = 0 

  while queue:
    x, y, dir = queue.popleft()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 범위내이고
    if(0 <= nx < n and 0 <= ny < n):
      # 1. 빈 칸 혹은 다른문(목표점)이면
      if(graph[nx][ny] == '.' or graph[nx][ny] == '#'):    
        # 1-1. 방문한적 없으면 
        if(visited[nx][ny][dir] == -1): 
          queue.append((nx, ny, dir))  # 같은 방향
          visited[nx][ny][dir] = visited[x][y][dir]
        # 1-2. 방문한적 있고 더 적은 거울을 사용했다면 업데이트
        else: 
          if(visited[nx][ny][dir] > visited[x][y][dir]):          
            queue.append((nx, ny, dir))  # 같은 방향
            visited[nx][ny][dir] = visited[x][y][dir]
      # 2. 거울 설치가 가능한 위치면 
      elif(graph[nx][ny] == '!'):
        # 2-1. 거울 설치X 
        # 2-1-1. 방문한적 없으면
        if(visited[nx][ny][dir] == -1):
          # 같은 방향으로 삽입, 방문 처리
          queue.append((nx, ny, dir))  # 같은 방향
          visited[nx][ny][dir] = visited[x][y][dir]
        # 2-1-2. 방문한적 있고 더 적은 거울을 사용했다면
        else:
          if(visited[nx][ny][dir] > visited[x][y][dir]):
            # 더 적은 거울을 사용한 현재값으로 업데이트
            queue.append((nx, ny, dir))  # 같은 방향
            visited[nx][ny][dir] = visited[x][y][dir]
        # 2-2. 거울 설치O
        for ndir in [(dir + 1) % 4, (dir + 3) % 4]:
          # 2-2-1. 방문한적 없으면 
          if(visited[nx][ny][ndir] == -1):
            # 같은 방향으로 삽입, 방문처리
            queue.append((nx, ny, ndir))
            visited[nx][ny][ndir] = visited[x][y][dir] + 1           # 2-2-2. 방문한적 있고 더 적은 거울을 사용했다면 
          else:
            if(visited[nx][ny][ndir] > visited[x][y][dir] + 1):
              # 더 적은 거울을 사용한 현재값으로 업데이트
              queue.append((nx, ny, ndir))
              visited[nx][ny][ndir] = visited[x][y][dir] + 1
  min_cnt = 1e9  # 최소 거울 개수
  # 최소 거울 개수 찾기
  for cnt in visited[end[0]][end[1]]:
    if(cnt == -1):  continue
    elif(min_cnt > cnt):  min_cnt = cnt
  return min_cnt
  
n = int(input())  # 집 크기
# n * n (#: 문, *: 벽, !: 거울설치가능, .:빈곳 )
graph = [list(input().strip()) for _ in range(n)]
# n * n * 4 (i행 j열 dir방향으로 올 때 필요한 거울 개수)
visited = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
# 북, 서, 남, 동(0, 1, 2, 3)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
start = (0, 0)  # 시작점
end = (0, 0)    # 목표점
doorNum  = 0    # 문 개수

# 문 위치 찾기
for i in range(n):
  # 2개 다 찾았으면 종료
  if(doorNum == 2):  break
  for j in range(n):
    if(graph[i][j] == '#'):
      # 첫번째 문이면 시작점으로
      if(doorNum == 0):
        start = (i, j)
        doorNum += 1
      else:
        end = (i, j)
        doorNum += 1
        break
    
print(bfs(start, end))