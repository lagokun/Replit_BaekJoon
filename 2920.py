N = list(map(int,input().split()))

a = [1,2,3,4,5,6,7,8]
b = [8,7,6,5,4,3,2,1]

if N == a:
  print('ascending')
elif N == b:
  print('descending')
else:
  print('mixed')
