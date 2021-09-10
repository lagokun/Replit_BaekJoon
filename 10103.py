n = int(input())
c=100
d=100

for i in range(n):
  a, b = list(map(int,input().split()))
  if a > b:
    c -= a
  elif a < b:
    d -= b
  else:
    pass

print(d)
print(c)
