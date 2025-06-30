import math
a = int(input("Muntazam Uchburchakning tomoni uchun son kiriting: "))
Amal = int(input("Qaysi birini topishni xohlaysiz? (1 - tomoni, 2 - ichki chizilgan aylana radiusi, 3 - tashqi chizilgan aylana radiusi, 4 - yuzasi)"
                 "Kiriting: "))
if a > 0:
  r1 =  a * pow(3,1/2) / 6
  r2 = 2 * r1
  s = pow(a,2) * pow(3,1/2) / 4
  match Amal:
    case 1:
      print(a)
    case 2:
      print(r1)
    case 3:
      print(r2)
    case 4:
      print(s)