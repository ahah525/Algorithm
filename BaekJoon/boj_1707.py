from collections import deque
import sys

# BFS
def bfs(v):
  queue = deque()
  # 시작점 삽입, 방문 처리
  queue.append(v)
  visited[v] = 0

  while queue:
    v = queue.popleft()
    # 인접 지점 탐색
    for i in graph[v]:
      # 방문하지 않은 노드이면 삽입, 방문 처리
      if(visited[i] == -1):
        queue.append(i)
        visited[i] = not visited[v]  # 비트 반전
      # 인접한 지점의 값이 같으면 바로 False 리턴
      elif(visited[i] == visited[v]): 
        return False
  return True

k = int(sys.stdin.readline())  # 테스트 케이스 수
for _ in range(k):
  v, e = map(int, sys.stdin.readline().split())  # 정점 수, 간선 수
  graph = [[] for _ in range(v + 1)]  # 정점들의 인접 노드
  # 방문 여부(-1: 방문 안함, 0, 1: 방문한 경우)
  visited = [-1] * (v + 1)

  # 간선 정보 입력받기
  for _ in range(e):
    u, v = map(int, sys.stdin.readline().split())  # 인접한 두 정점
    graph[u].append(v)
    graph[v].append(u)

  flag = True  # 이분 그래프 여부
  for i in range(1, v + 1):
    if(visited[i] == -1):
      # 하나라도 False이면
      if not bfs(i):
        flag = False
        break
        
  if(flag == True):  print("YES")
  else:  print("NO")
  