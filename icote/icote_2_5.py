n, m = map(int, input().split())  # 맵 크기
x, y, d = map(int, input().split())  # 현재 좌표, 방향(0, 1, 2, 3)
# n*m 맵 정보(0: 육지, 1: 바다, 2: 가봄)
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 1  # 현재 방문 횟수를 1로 초기화(시작 지점 체크)
turn = 0  # 회전 횟수
arr[x][y] = 2  # 시작 지점 방문 표시

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전 함수
def turn_left():
  global d  # 현재 방향
  d -= 1  # 왼쪽 회전
  
  if(d == -1):  # 인덱스 아웃되는 경우 처리
    d = 3
  
# 시뮬레이션 시작
while True:
  # 왼쪽 회전
  turn_left()
  # 검사할 칸(앞) 좌표
  nx = x + dx[d]
  ny = y + dy[d]

  # 안가본 칸이면 전진
  if(arr[nx][ny] == 0):    
    # 앞으로 1칸 이동
    x, y = nx, ny
    arr[x][y] = 2  # 방문 표시
    cnt += 1  # 방문 횟수 카운팅
    turn = 0  # 회전 횟수 초기화(이동했으므로)
    continue
  else:
    turn += 1  # 회전 횟수 카운팅

  # 4방향 모두 가봤거나 바다이면 후진
  if(turn == 4):    
    # 검사할 칸(뒤) 좌표
    nx = x - dx[d]
    ny = y - dy[d]
  
    # 뒤로 갈 수 있으면(바다 아니면)
    if(arr[nx][ny] != 1):
      # 뒤로 1칸 이동 (이전에 왔던 칸이므로 방문 횟수 카운팅 하지 않음)
      x, y = nx, ny
      arr[x][y] = 2
      turn = 0  # 회전 횟수 초기화
    # 뒤로 갈 수 없으면
    else:
      # 탈출 
      break
    turn = 0

print(cnt)  # 총 방문 칸 수