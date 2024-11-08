import math
a = int(input("A uchun qiymat kiriting: "))
p = "radian qiymatda"
if a > 0 and a < 360:
  print("Qiymat radianda hisoblanganda: " + str(a * math.pi/180))
else:
  print("Kiritilgan qiymat 0 va 360 oralig'ida gradus uchun mo'ljallangan bo'lishi kerak.")