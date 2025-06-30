import math
a = int(input("Teng yonli Uchburchakning kateti uchun son kiriting: "))
Amal = int(input("Qaysi birini topishni xohlaysiz? (1 - katet, 2 - gipotenuza, 3 - gipotenuzaga tushirilgan balandlik, 4 - yuzasi)"
                 "Kiriting: "))
if a > 0:
  c = a*pow(2,1/2)
  h = c/2
  match Amal:
    case 1:
      print(a)
    case 2:
      print(c)
    case 3:
      print(h)
    case 4:
      print(c*h/2)