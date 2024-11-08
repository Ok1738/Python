import math
r1 = int(input("Birinchi radius uchun qiymat kiritng: "))
r2 = int(input("Ikkinchi radius uchun qiymat kiritng: "))
if r1 > r2:
  s1 = r1 * math.pi
  s2 = r2 * math.pi
  print("Radiuslar yuzalari ayirmasi: " + str(s2 - s1))
else: 
  print("Birinchi kiritilgan qiymat ikkinchisidan katta bo'lishi zarur.")