import heapq
import sys

n = int(input())  # 수업 수
# n 개의 수업 정보
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
schedule.sort()   # 시작값 기준 오름차순 정렬
 
room = []  # 강의실에 배치한 수업
heapq.heappush(room, schedule[0][1])  # 끝값 추가

for i in range(1, n):
  # 다른 강의 끝값 최솟값이 현재 강의 시작값보다 크다면
  if(room[0] > schedule[i][0]):
    # 새로운 강의실에 배치
    heapq.heappush(room, schedule[i][1])  # 현재 강의 끝값 추가
  # 다른 강의 끝값 최솟값이 현재 강의 시작값보다 작거나 같다면
  else:
    # 현재있는 강의실에 배치(변경=삭제->추가)
    heapq.heappop(room)  # 변경할 강의 삭제
    heapq.heappush(room, schedule[i][1])  # 현재 강의 끝값 추가

print(len(room))
