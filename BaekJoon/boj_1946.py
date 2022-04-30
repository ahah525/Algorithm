import sys

t = int(input())  # 테스트 케이스 수

for _ in range(t):
  n = int(input())  # 지원자 수
  # n개의 지원자 서류, 면접 순위(2차원 리스트)
  arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

  # 오름차순 정렬(서류 기준)
  arr.sort(key = lambda x : x[0])

  cnt = 1  # 선발 인원 수
  high_rank = arr[0][1]  # 면접 최고 순위
  for i in range(1, n):
    rank = arr[i][1]  # 현재 면접 순위
    # 면접 순위 1위이면 선발
    if(rank == 1):
      cnt += 1
      high_rank = rank  # 높은 랭크 갱신
      continue
    # 현재 면접 순위가 면접 최고 순위보다 높으면
    if(rank < high_rank):
      cnt += 1
      high_rank = rank  # 높은 랭크 갱신
      
  print(cnt)  