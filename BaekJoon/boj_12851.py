from collections import deque

# BFS
def bfs(x, cnt):
  min_time = 0  # 최소 시간
  num = 0       # 방법수
  queue = deque()
  # 시작 위치 삽입, 방문처리
  queue.append((x, cnt))
  visited[x] = 1
  
  while queue:
    x, cnt = queue.popleft()
    visited[x] = 1  # 방문 처리
    # 동생을 찾으면 종료
    if(x == k):
      # 처음 발견하면
      if(min_time == 0): 
        min_time = cnt  # 최소시간 설정
        num += 1        # 방법수 카운트
      # 2번째 이상 발견한 시간이 최소시간과 같다면 
      elif(min_time == cnt):
        num += 1        # 방법수 카운트만
      # 2번째 이상 발견한 시간이 최소시간과 다르면(최소시간보다 무조건 크므로) 종료
      else:   break 

    for nx in [x - 1, x + 1, 2 * x]:
      if(0 <= nx <= 100000):
        # 방문한적이 없으면
        if(visited[nx] == 0):
          queue.append((nx, cnt + 1))  # 삽입만
  return (min_time, num)  # 종료 시 최소 시간, 방법수 리턴
  
n, k = map(int, input().split())  # 수빈, 동생 위치
visited = [0] * (100001)
for i in bfs(n, 0):
  print(i)