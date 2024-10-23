import math
x1 = int( input("1) X uchun son kiriting: ") )
y1 = int( input("1) Y uchun son kiriting: ") )
x2 = int( input("2) Yana X uchun son kiriting: ") )
y2 = int( input("2) Yana Y uchun son kiriting: ") )
x3 = int( input("3) Yana X uchun son kiriting: ") )
y3 = int( input("3) Yana Y uchun son kiriting: ") )

a = math.sqrt(pow(x2 - x1, 2) + pow(y2 -y1, 2))
b = math.sqrt(pow(x3 - x1, 2) + pow(y3 -y1, 2))
c = math.sqrt(pow(x2 - x3, 2) + pow(y2 -y3, 2))

p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))

print("Yuzasi: " + str(S))
print("Perimetri: " + str(p))