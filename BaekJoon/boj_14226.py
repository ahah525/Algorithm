from collections import deque

# BFS
def bfs(screen, board, time):
  queue = deque()
  # 시작점 삽입, 방문 처리
  queue.append((screen, board, time))
  graph.add((screen, board))
  
  while queue:
    screen, board, time = queue.popleft()
    # 화면의 이모티콘 개수가 목표치에 도달하면
    if(screen == s):
      return time

    # 화면과 클립보드 수가 범위 내이고 
    # (화면, 보드) 쌍이 방문한 적이 없으면 
    # 큐에 (화면, 보드, 시간) 쌍 삽입, 그래프에 (화면, 보드) 쌍 삽입
    # 1. 화면에 있는 모든 이모티콘을 클립보드에 저장
    if(1 <= screen <= 1000):
      if((screen, screen) not in graph):  
        queue.append((screen, screen, time + 1))
        graph.add((screen, screen))
    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
    if(1 <= screen + board <= 1000 and 0 < board):
      if((screen + board, board) not in graph):
        queue.append((screen + board, board, time + 1))
        graph.add((screen + board, board))
    # 3. 화면에 있는 이모티콘 중 하나를 삭제
    if(1 <= screen - 1 <= 1000):
      if((screen - 1, board) not in graph):
        queue.append((screen - 1, board, time + 1))
        graph.add((screen - 1, board))

s = int(input())  # 이모티콘 개수
graph = set()     # 방문한 (화면, 보드) 쌍을 담을 집합
print(bfs(1, 0, 0))  # 화면 이모티콘 1, 클립보드 이모티콘 0개, 시간 0으로 시작
