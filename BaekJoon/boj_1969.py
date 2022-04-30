from collections import Counter

n, m = map(int, input().split())  # DNA 수, 문자열 길이
dna = [list(input()) for _ in range(n)]
# 2차원 리스트 행과 열 바꾸기
dna = list(map(list, zip(*dna)))

cnt = 0  # HD의 합
min_dna = ""  # HD의 합이 최소가되는 dna 
for i in range(m):
  # 가장 빈도수가 높은 문자 추출해서 dna 만들기
  counts = Counter(sorted(dna[i]))
  c = counts.most_common(1)[0][0]  # 가장 빈도수가 높은 문자
  num = counts.most_common(1)[0][1]  # 해당 문자의 빈도 수
  cnt += (n - num)  # 가장 빈도수가 높은 문자를 제외한 문자 수
  min_dna += c

print(min_dna)
print(cnt)


'''
n, m = map(int, input().split())  # DNA 수, 문자열 길이
dna = [list(input()) for _ in range(n)]

# 4가지 문자
type = ('A', 'C', 'G', 'T')
cnt = 0  # HD의 합
min_dna = ""  # HD의 합이 최소가되는 dna 

# 리스트 열 기준 검사하기
for i in range(m):
  num = [0] * 4  # 빈도수
  # j번째 인덱스에 대한 각 행 문자 검사하기
  for j in range(n):
    for k in range(4):
      # 문자 빈도수 세기
      if(dna[j][i] == type[k]):
        num[k] += 1
        break

  # HD가 최소가 되는 DNA
  cnt += n - max(num)  # HD 값
  min_dna += type[num.index(max(num))]  # 최댓값의 인덱스에 해당하는 문자
    
print(min_dna)
print(cnt)

'''