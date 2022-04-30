n = int(input())    # 카드 개수
l = list(map(int, input().split()))  # 카드 레벨
l.sort(reverse = True)  # 내림차순 정렬
max = l[0]  # 최댓값

gold = max * (n - 1) + sum(l[1:])
print(gold)

'''
n = int(input())    # 카드 개수
l = list(map(int, input().split()))  # 카드 레벨
gold = 0  # 골드 수
max = max(l)  # 최고 레벨
max_idx = l.index(max)  # 최고 레벨 인덱스

while True:
  n = len(l)  # 남은 카드 수
  target = 0  # 합성할 카드
  
  # 카드가 1장밖에 안남았으면 탈출
  if(n == 1):
    break

  # 맨 끝 인덱스가 아니면 오른쪽 합성
  if(0 <= max_idx < n - 1):
    target = l[max_idx + 1]
    gold += (max + target)
    del l[max_idx + 1]  # 합성 카드 삭제
  # 맨 끝 인덱스이면 왼쪽 합성
  elif(max_idx == n - 1):
    target = l[max_idx - 1]
    gold += (max + target)
    del l[max_idx - 1]  # 합성 카드 삭제
    max_idx -= 1  # 최댓값 인덱스 수정
      
print(gold)
'''