n = int(input())

p_list = [0 for i in range(n+1)]
p_list[1] = 1

for i in range(2,n+1):
  p_list[i] = p_list[i-1] + p_list[i-2]

print(p_list[n])
