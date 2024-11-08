import math
a = int(input("A uchun son kiriting: "))
b = int(input("B uchun son kiriting: "))
c = int(input("C uchun son kiriting: "))
d = pow(b,2) - 4*a*c
if d > 0:
 print( str(a) + 'x^2 + ' + str( b) + 'x + ' + str(c) + " = 0 tenglamaning birinchi yechimi: " + str( (-b + math.sqrt(d))/2*a ) + ", ikkinchi yechimi: " + str( (-b - math.sqrt(d))/2*a ) )
else: 
  print( str(a) + 'x^2 + ' + str( b) + 'x + ' + str(c) + " = 0 tenglamaning deskriminanti noldan katta bo'lishi kerak.")