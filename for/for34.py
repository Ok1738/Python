n = int(input("N sonini kiriting: "))
if n > 1: 
  A_1 = 1
  A_2 = 2
  for k in range(3, n+1):
    A_k = (A_1 + (2*A_2)) / 3
    A_1 = A_2
    A_2 = A_k
    print(A_k)