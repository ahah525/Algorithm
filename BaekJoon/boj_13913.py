from collections import deque

# BFS
def bfs(x, cnt):
  queue = deque()
  # 시작 지점 삽입, 방문 처리
  queue.append((x, cnt))
  visited[x] = 0  # 이전 방문값이 없음

  while queue:
    x, cnt = queue.popleft()
    
    # 끝점에 도달하면 종료
    if(x == k):
      return cnt  # 최소 시간 리턴
      
    for nx in [x - 1, x + 1, 2 * x]:
      if(0 <= nx <= 100000):
        # 방문한적이 없으면
        if(visited[nx] == -1):
          # 삽입, 방문 처리
          queue.append((nx, cnt + 1))    
          visited[nx] = x  # 이전 값 기록 
          
n, k = map(int, input().split())  # 시작점, 끝점
visited = [-1] * (100001)  # 방문 여부
min_time = bfs(n, 0)
path = [] # 최단 경로
print(min_time)

i = k  # 끝점으로 초기화
# 역순으로 경로 탐색 저장하기
for _ in range(min_time + 1):
  path.append(i)  
  i = visited[i]
# 경로 역순으로 출력하기
for i in range(min_time, -1, -1):
  print(path[i], end = " ")