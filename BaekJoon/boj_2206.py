from collections import deque
# 세로, 가로
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 3차원 리스트(0: 방문하지 않은 곳, 1: 방문한 곳)
# visited[0][0][0]: 벽 파괴 가능, visited[0][0][1]: 벽 파괴 불가능
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]  # 3차원 행렬
visited[0][0][0] = 1
visited[0][0][1] = 1

# BFS(현재 좌표, 부순 위치)
def bfs(x, y, c):
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  queue.append((x, y, c))
  
  while queue:
    x, y, c = queue.popleft()
    #print(x, y, c)
    # 끝 점에 도달하면(종료 조건)
    if(x == n - 1 and y == m - 1):
      return visited[x][y][c]  # 이동 칸 수
    # 상하좌우 탐색
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < n and 0 <= ny < m):
        # 길이고 아직 방문하지 않은 곳이면
        if(graph[nx][ny] == 0 and visited[nx][ny][c] == 0):
          # 삽입, 방문 처리
          queue.append((nx, ny, c))
          visited[nx][ny][c] = visited[x][y][c] + 1
        # 벽이고 아직 벽을 부순적이 한 번도 없으면
        elif(graph[nx][ny] == 1 and c == 0):
          # 해당 좌표 벽 부수기          
          queue.append((nx, ny, 1)) 
          visited[nx][ny][1] = visited[x][y][0] + 1
  return -1
 
# 시작 지점(0,0)에서 아직 벽을 부수지 않은 상태로 호출
print(bfs(0, 0, 0))