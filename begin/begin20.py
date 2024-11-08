import math
x1 = int( input("X uchun son kiriting: ") )
y1 = int( input("Y uchun son kiriting: ") )
x2 = int( input("Yana X uchun son kiriting: ") )
y2 = int( input("Yana Y uchun son kiriting: ") )
print("Ikki nuqta orasidagi masofa: " + str(math.sqrt(pow(x2 - x1, 2) + pow(y2 -y1, 2))))