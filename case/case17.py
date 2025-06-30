a = int(input("Son kiriting: "))
if a >= 10 and a <= 40:
  onliklar = a // 10
  birliklar = a % 10
  match onliklar:
      case 2:
        print("Yigirma", end="")
      case 3:
        print("O'ttiz", end="")
      case 4:
        print("Qirq", end="")
  match birliklar:
        case 0: 
          print("ta masala.")
        case 1:
          print(" bitta masala.")
        case 2:
          print(" ikkita masala.")
        case 3:
          print(" uchta masala.")
        case 4:
          print(" to'rtta masala.")
        case 5: 
          print(" beshta masala.")
        case 6:
          print(" oltita masala.")
        case 7:
          print(" yettita masala.")
        case 8:
          print(" sakkizta masala.")
        case 9:
          print(" to'qqizta masala.")
else: 
  print("Boshqattan urinib ko'ring!")
  
      