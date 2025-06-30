n = int(input("N uchun son kiriting: "))
if n > 1:
  F_1 = 1
  F_2 = 1
  for k in range(3, n+1):
    F_k = F_1 + F_2 
    F_1 = F_2
    F_2 = F_k
    print(F_k)
    
    
    