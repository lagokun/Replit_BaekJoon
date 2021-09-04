N, B = int(input()), list(map(int,input().split()))


A = []

for i in range(len(B)):
  A.append(B[i]*(i+1))

for j in reversed(range(1, len(A))):
  A[j] = A[j] - A[j-1]

for k in range(len(A)):
  print(A[k], end = ' ')
