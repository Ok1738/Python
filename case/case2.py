k = int(input("Son kiriting: "))
if k <= 5 and k >= 1:
  match k:
    case 1:
         print("Yomon.")
    case 2:
         print("Qoniqarsiz.")
    case 3:
         print("Qoniqarli.")
    case 4:
        print("Yaxshi.")
    case 5:
        print("A'lo.")
else:
  print("xato.")