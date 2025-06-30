x = int(input("Son kiriting: "))
if x <= 7 and x >= 1:
  match x:
    case 1:
         print("Dushanba")
    case 2:
         print("Seshanba")
    case 3:
         print("Chorshanba")
    case 4:
        print("Payshanba")
    case 5:
        print("Juma")
    case 6:
        print("Shanba")
    case 7:
        print("Yakshanba")
else:
  print("1 va 7 oralig'ida son kiritish kerak.")