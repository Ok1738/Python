n = int(input())
if n > 2:
  A_1 = 1
  A_2 = 2
  A_3 = 3
  for k in range(4, n+1):
    A_k = A_3 + A_2 - (2*A_1)
    A_1 = A_2
    A_2 = A_3
    A_3 = A_k
    print(A_k)
    
    
  