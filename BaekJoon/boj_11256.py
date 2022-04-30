t = int(input())  # 테스트 케이스 수

for i in range(t):
  j, n = map(int,input().split())  # 사탕 개수, 상자 개수
  box = []  # n개의 박스 크기
  res = 0 # 박스 개수
  for _ in range(n):
    box.append(list(map(int, input().split())))  # 세로, 가로 길이
    
  # 박스 부피 기준 내림차순 정렬
  box.sort(key=lambda x : x[0] * x[1], reverse = True)

  # 최소 박스 개수 세기
  for b in box:
    # 사탕이 0개가 되면 탈출
    if(j == 0):
      break
    volume = b[0] * b[1]  # 박스 부피
    if(j >= volume):
      j -= volume  # 박스 부피만큼 차감
      res += 1     # 박스 개수 추가
    else:
      j -= j  # 사탕 개수만큼 차감
      res += 1     # 박스 개수 추가
    
  print(res)  # 최소 박스 개수