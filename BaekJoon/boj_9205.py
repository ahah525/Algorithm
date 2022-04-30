from collections import deque

# BFS
def bfs():
  queue = deque()
  # 시작점 삽입
  queue.append((start[0], start[1]))

  while queue:
    x, y = queue.popleft()
    # 끝점과의 거리가 1000이하이면 성공(탈출 조건)
    if(abs(x - end[0]) + abs(y - end[1]) <= 1000):
      return True

    for i in range(n):
      # 방문한적이 없고
      if(visited[i] == 0):
        # 거리가 1000이내이면 삽입, 방문 처리
        if(abs(x - graph[i][0]) + abs(y - graph[i][1]) <= 1000):
          queue.append((graph[i][0], graph[i][1]))
          visited[i] = 1
  return False

t = int(input())  # 테스트 케이스 수
for _ in range(t):
  res = True  # 여부
  n = int(input())  # 편의점 개수
  start = list(map(int, input().split())) # 시작점
  graph = [list(map(int, input().split())) for _ in range(n)]  # 편의점
  end = list(map(int, input().split())) # 끝점
  visited = [0] * (n + 1)  # 편의점 방문 여부
  
  res = bfs()
  if res:  print("happy")
  else:  print("sad")
    
  