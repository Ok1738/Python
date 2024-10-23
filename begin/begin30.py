import math
a = int(input("A uchun qiymat kiriting: "))
p = "radian qiymatda"
if a > 0 and a < 360:
  print("Qiymat gradusda hisoblanganda: " + str(a * 180/math.pi))
else:
  print("Kiritilgan qiymat 0 va 2п oralig'ida radian uchun mo'ljallangan bo'lishi kerak.")