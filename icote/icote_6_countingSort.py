# 계수 정렬(Counting Sort)
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) + 1)  # 모든 범위를 포함하는 리스트

# 오름차순 정렬
for i in array:
  count[i] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end = " ")
