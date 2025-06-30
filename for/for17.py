import math
c = 0
n = int(input("Daraja uchun son kiriting: "))
a = float(input("Asos uchun son kiriting:: "))
for x in range(n+1):
  print(pow(a, x))
  c += pow(a, x)
print(f"{a} ning darajalarida hisoblanganda, yig'indi {c} ga to'g'ri kelmoqda.")