from collections import deque

# BFS(현재값, 연산횟수)
def bfs(x, c):
  queue = deque()
  queue.append((x, c))

  while queue:
    x, c = queue.popleft()
    # B에 도달하면 종료
    if(x == b): 
      return c + 1
    # 2를 곱한 값, # 오른쪽에 1을 추가한 값
    dx = [2 * x, int(str(x) + "1")]
    
    for nx in dx:
      # 1보다 크고 목표값보다 작거나 같으면
      if(1 < nx <= b):
        # 삽입, 방문 처리
        queue.append((nx, c + 1))
  return -1     

a, b = map(int, input().split())  # 시작값, 목표값
print(bfs(a, 0))