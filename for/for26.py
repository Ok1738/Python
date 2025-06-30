import math
n = int(input("Daraja va maxraj uchun son kiriting (n): "))
x = float(input("Son kiriting (x): "))
temp = 0
if n > 0 and abs(x) < 1:
  for i in range(n):
    temp += (((-1) ** i ) * (x ** (2*i+1))) / (2*i + 1)
  print(temp)
    
    



  