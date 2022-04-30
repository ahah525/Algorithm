a, p = map(int, input().split())  # 첫번째 수, 제곱
d = [a]  # 반복 수열
i = 0
start = 0  # 반복 시작 지점
while True:
  num = 0 
  # 각 자리숫자를 P번 곱한 수들의 합
  for n in str(d[i]) :
    num += int(n)**p
  # 현재 숫자가 d에 이미 있는 숫자라면(탈출 조건)
  if num in d:
    start = d.index(num)
    break
  # 현재 숫자가 d에 없다면 리스트에 넣고 인덱스 변경
  d.append(num)
  i += 1

print(start)
