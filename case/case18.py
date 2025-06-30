a = int(input("Son kiriting: "))
if a >= 100 and a <= 999:
  onliklar = a // 10 % 10
  yuzlikar = a // 100
  birliklar = a % 10
  match yuzlikar:
    case 1:
      print(" Biryuz ",end="")
    case 2:
      print(" Ikkiyuz ",end="")
    case 3:
      print(" Uchyuz ",end="")
    case 4:
      print(" To'rtyuz ",end="")
    case 5: 
      print(" Beshyuz ",end="")
    case 6:
      print(" Oltiyuz ",end="")
    case 7:
      print(" Yettiyuz ",end="")
    case 8:
      print(" Sakkizyuz ",end="")
    case 9:
      print(" To'qqizyuz ",end="")
  match onliklar:
      case 1:
        print( "o'n ", end="")
      case 2:
        print("Yigirma ", end="")
      case 3:
        print("O'ttiz ", end="")
      case 4:
        print("Qirq ", end="")
      case 5:
        print("Ellik ", end="")
      case 6:
          print("Oltmish ", end="")
      case 7:
        print(" yetmish", end="")
      case 8:
        print(" sakson", end="")
      case 9:
        print(" to'qson", end="")
  match birliklar:
        case 1:
          print(" bir")
        case 2:
          print(" ikki")
        case 3:
          print(" uch")
        case 4:
          print(" to'rt")
        case 5: 
          print(" besh")
        case 6:
          print(" olti")
        case 7:
          print(" yetti")
        case 8:
          print(" sakkiz")
        case 9:
          print(" to'qqiz")
else: 
  print("Boshqattan urinib ko'ring!")
  
      