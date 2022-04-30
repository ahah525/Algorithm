n = int(input())  # 줄 개수
powers = [int(input()) for _ in range(n)]  # 각 줄의 최대 중량
powers.sort(reverse = True)  # 내림차순 정렬

for i in range(n):
  powers[i] *= (i + 1)
print(max(powers))