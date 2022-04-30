n = int(input())
cnt = 0    # 종말 숫자 개수
num = 666  # 가장 작은 종말수

while True:
  # 666이 있으면 개수 세기
  if '666' in str(num):
    cnt += 1
  # n번째로 작은 종말수이면 출력 종료
  if cnt == n:
    print(res)
    break
  num += 1
