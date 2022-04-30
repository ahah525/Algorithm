from collections import deque

n, m = map(int, input().split())  # 세로, 가로
# 0: 갈 수 없는 곳, 1: 갈 수 있는 곳
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  # 큐 구현을 위한 deque 라이브러리 사용
  queue = deque()
  queue.append((x, y))  # 현재 노드 삽입
  
  while queue:
    x, y = queue.popleft()  # 가장 오래된 노드 꺼내기
    
    # 종료 지점에 도착하면(종료 조건)
    if(x == n - 1 and y == m - 1):   
      return graph[n - 1][m - 1]  # 최소 이동 칸 개수 출력
    
    # 상하좌우 탐색
    for i in range(4):
      # 탐색할 인접 좌표
      nx = x + dx[i]
      ny = y + dy[i]

      # 좌표가 범위 내이면
      if(0 <= nx < n and 0 <= ny < m):
        # 갈 수 있는 곳이고 시작 위치가 아니라면
        if(graph[nx][ny] == 1 and [nx, ny] != [0, 0]):
          queue.append((nx, ny))  # 노드 삽입
          graph[nx][ny] = graph[x][y] + 1  # 방문처리

print(bfs(0, 0))  # 시작점 좌표에서 호출
'''
for i in graph:
  print(i)
'''