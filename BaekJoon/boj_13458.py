import math

n = int(input())  # 시험장 개수
arr = list(map(int, input().split()))  # 각 시험장 응시자 수
b, c = map(int, input().split())  # 총감독관, 부감독관 감시 인원 수
cnt = n  # 총 감독관 수는 시험장 개수만큼 초기화

for i in arr:
  people = (i - b)  # 부감독관이 관리해아할 총 인원 
  # 응시자 수가 0보다 크면
  if(people > 0):
    # 부감독관 수 반올림
    if(people % c == 0):
      cnt += people // c
    else:
      cnt += (people // c) + 1
    #cnt += math.ceil(people / c)  # 필요한 부감독관 수
print(cnt)
