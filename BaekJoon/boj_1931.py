n = int(input())  # 회의 수
info = [list(map(int, input().split())) for _ in range(n)]  # n개의 회의 정보
# 끝나는 시간, 시작 시간 기준 오름차순 정렬
info.sort(key=lambda x : (x[1], x[0]))
start = 0  # 회의 시작 가능 시간
cnt = 0  # 회의 개수
#arr= []  # 선택된 회의들

# start 이상 값 중 끝나는 시간이 가장 작은 회의 찾기
# i: 현재 시작 시간, j: 현재 끝나는 시각
for i, j in info:
  # 현재 시작 시간이 시작 가능 시간 이상이면
  if(start <= i):
    cnt += 1
    # 다음 회의 시작 가능 시간을 현재 회의 끝나는 시간으로 변경
    start = j 
    #arr.append([i, j])
    
print(cnt)  # 회의 최대 개수 출력
#print(arr)