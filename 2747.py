n = int(input())

f_list = [0 for i in range(n+1)]
f_list[1] = 1

for i in range(2,n+1):
  f_list[i] = f_list[i-1] + f_list[i-2]

print(f_list[n])
