N = int(input())

num_list = []

for i in range(N):
  num = input().split()
  num_list.append([int(num[0]), int(num[1])])

#기본 정렬 라이브러리는 기본적으로 튜플의 인덱스 순서를 따름
num_list.sort()

for i in num_list:
  print(i[0], i[1])
