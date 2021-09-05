N = int(input())

mem_list = []

for i in range(N):
  member = input().split()
  mem_list.append([int(member[0]), member[1]])

mem_list.sort(key = lambda x: x[0])

for i in range(len(mem_list)):
  print(mem_list[i][0], mem_list[i][1])
