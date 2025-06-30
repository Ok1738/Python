a = int(input("Son kiriting: "))
if a >= 20 and a <= 69:
  onliklar = a // 10
  birliklar = a % 10
  match onliklar:
      case 2:
        print("Yigirma", end="")
      case 3:
        print("O'ttiz", end="")
      case 4:
        print("Qirq", end="")
      case 5:
        print("Ellik", end="")
      case 6:
          print("Oltmish", end="")
  match birliklar:
        case 0: 
          print(" yosh.")
        case 1:
          print(" bir yosh.")
        case 2:
          print(" ikki yosh.")
        case 3:
          print(" uch yosh.")
        case 4:
          print(" to'rt yosh.")
        case 5: 
          print(" besh yosh.")
        case 6:
          print(" olti yosh.")
        case 7:
          print(" yetti yosh.")
        case 8:
          print(" sakkiz yosh.")
        case 9:
          print(" to'qqiz yosh.")
else: 
  print("Boshqattan urinib ko'ring!")
  
      