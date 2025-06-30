n = int(input())
if n > 0:
  A_0 = 2
  for k in range(1, n+1):
    A_n = 2 + 1 / A_0
    A_0 = A_n
    print(A_n)