import math
n = int(input("n uchun son kiriting: "))
x = float(input("x uchun Son kiriting: "))
temp = 0
if n > 0 and abs(x) < 1:
  for i in range(1,n+1):
    temp += (((-1) ** (i - 1) ) * (x ** (i)) ) / i
  print(temp)
else: 
  print("Boshqattan urinib ko'ring! ")


  