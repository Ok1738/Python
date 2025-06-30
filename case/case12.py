import math
R = int(input("Doiraning radiusi uchun son kiriting: "))
Amal = int(input("Qaysi birini topishni xohlaysiz? (1 - radius, 2 - diameter, 3 - uzunligi, 4 - yuzasi)"
                 "Kiriting: "))
match Amal:
  case 1:
    print(R)
  case 2:
    print(2*R)
  case 3:
    print(2*math.pi*R)
  case 4:
    print(math.pi*pow(R,2))