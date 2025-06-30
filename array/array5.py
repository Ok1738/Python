n = int(input())
F = [None] * n
F[0] = F[1] = 1
k = 2
while True:
  F[k] = F[k-1] + F[k-2]
  k += 1
  if k == n:
    break
print(F)