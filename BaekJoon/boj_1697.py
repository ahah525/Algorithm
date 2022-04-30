from collections import deque
# 수빈, 동생 위치
n, k = map(int, input().split())
graph = [0] * (100001)

# BFS
def bfs(x):
  queue = deque()

  # 시작 지점 삽입, 방문 처리
  queue.append(x)
  graph[x] = 1

  while queue:
    x = queue.popleft()
    if(x == k):
      break
    # 이동 방식 3가지
    nx = [x - 1, x + 1, x * 2]
    
    for i in nx:
      if(0 <= i <= 100000):
        # 방문하지 않은 곳이면
        if(graph[i] == 0):
          # 삽입, 방문 처리
          queue.append(i)
          graph[i] = graph[x] + 1
        
bfs(n)
print(graph[k] - 1)