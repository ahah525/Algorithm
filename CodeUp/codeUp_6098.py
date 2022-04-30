# 맵(0: 길, 1: 벽/장애물, 2: 먹이)
# 10 * 10 맵 입력
maze = [list(map(int, input().split())) for _ in range(10)]
x, y = 1, 1  # 현재 좌표(시작 지점으로 초기화)
maze[x][y] = 9  # 현재 좌표 방문 표시

while True:
    # 탈출 조건
    # 맨 오른쪽, 아래이면
    if ((nx == 8 and ny == 8)):
        break

    # 오른쪽 검사
    # 오른쪽이 길이면
    if (maze[x][y + 1] == 0):
        maze[x][y + 1] = 9  # 방문 표시
        y += 1  # 오른쪽 이동
    # 오른쪽이 벽이면
    elif (maze[x][y + 1] == 1):
        # 아래쪽이 길이면
        if (maze[x + 1][y] == 0):
            maze[x + 1][y] = 9  # 방문 표시
            x += 1  # 오른쪽 이동
        # 아래쪽이 벽이면 탈출
        elif (maze[x][y] == 1):
            break
        # 아래쪽이 먹이면 탈출
        elif (maze[x][y] == 2):
            maze[x + 1][y] = 9  # 방문 표시
            x += 1  # 오른쪽 이동
            break
    # 오른쪽 먹이면 탈출
    elif (maze[x][y + 1] == 2):
        maze[x][y + 1] = 9  # 방문 표시
        y += 1  # 오른쪽 이동
        break

# 맵 출력
for i in range(10):
    for j in range(10):
        print(maze[i][j], end=" ")
    print()
