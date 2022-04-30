n, k = map(int, input().split())  # 배열 크기, swap 연산 횟수
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

# A 오름차순 정렬, B 내림차순 정렬
a.sort()
b.sort(reverse=True)
# 두 배열의 원소 k번 비교
for i in range(k):
  # a가 b보다 크거나 같으면 swap 종료
  if a[i] >= b[i]:  break
  a[i], b[i] = b[i], a[i]
print(sum(a))