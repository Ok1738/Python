a = float(input("Son kiriting: "))
b = float(input("Son kiriting: "))
arifmetik_amal = int(input("Arifmetik amallarni bajarish uchun son kiriting: "))
if arifmetik_amal <= 4 and arifmetik_amal >= 1:
  match arifmetik_amal:
    case 1:
      print(a+b)
    case 2:
      print(a-b)
    case 3:
      print(a/b)
    case 4:
      print(a*b)