n = int(input())  # 2진 수열 크기
d = [1, 2]
for i in range(2, n):
  d.append((d[i - 1] + d[i - 2]) % 15746)
print(d[n - 1])

'''
n = int(input())  # 2진 수열 크기
d = [0] * 1000000
d[0], d[1] = 1, 2
for i in range(2, n):
  d[i] = (d[i-1] + d[i-2]) % 15746
print(d[n - 1])
'''