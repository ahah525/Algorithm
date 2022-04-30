n = int(input())  # 학생 수
arr = [input().split()  for _ in range(n)]  # n명의 학생정보

# 성적을 기준으로 오름차순 정렬
arr.sort(key=lambda x: x[1])
for student in arr:
  print(student[0], end= " ")  # 이름 출력

'''
# 2. 계수 정렬
n = int(input())  # 학생 수
arr = [[] for _ in range(101)]  # 성적은 100이하 자연수

for i in range(n):
  name, score = input().split()
  arr[int(score)].append(name)  # 해당 점수에 이름 넣기

for student in arr:
  for name in student:
    print(name, end=" ")
'''