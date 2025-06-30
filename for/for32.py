n = int(input("N uchun son kiriting: "))
if n > 0:
  A_0 = 1
  for k in range(1, n+1):
    A_k = (A_0 + 1) / k
    print(A_k)
    A_0 = A_k
    