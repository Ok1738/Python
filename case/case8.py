a = int(input("Kunni aniqlash uchun son kiriting: ")) #kun
b = int(input("Oyni aniqlash uchun son kiriting: ")) #oy 
birliklar = a % 10 
onliklar = a //10
if b == 2:
  if (a >= 1 and a <= 28):
    match onliklar:
        case 1:
          print("O'ninchi ", end="")
        case 2:
          print("Yigirmanchi ", end="")
    match birliklar:
        case 1:
          print("Birinchi", end="")
        case 2:
          print("Ikkinchi", end="")
        case 3:
          print("Uchinchi", end="")
        case 4:
          print("To'rtinchi", end="")
        case 5:
          print("Beshinchi", end="")
        case 6:
          print("Oltinchi", end="")
        case 7:
          print("Yettinchi", end="")
        case 8:
          print("Sakkizinchi", end="")
        case 9:
          print("To'qqizinchi", end="")
    print(" Fevral.")
  elif (a == 29):
    print("Kiritilgan sana Kabisa yilda bo'lmasligi kerak.")
  elif (a <= 0):
    print("Boshqattan urinib ko'ring! Fevral oyi musbat kunlardan iborat.")
  else:
    print("Boshqattan urinib ko'ring! Fevral oyi 29 kundan ortiq bo'la olmaydi.")
elif (b == 4 or b == 6 or b == 9 or b == 11):
  if a > 30:
    print("Boshqattan urinib ko'ring! Bu oy 30 kundan ortiq bo'la olmaydi.")
  elif not( a == 10 or a == 20 or a == 30):
    match onliklar:
          case 1:
            print("O'n ", end="")
          case 2:
            print("Yigirma ", end="")
          case 3:
            print("O'ttiz ", end="")
    match birliklar:
        case 1:
          print("Birinchi", end="")
        case 2:
          print("Ikkinchi", end="")
        case 3:
          print("Uchinchi", end="")
        case 4:
          print("To'rtinchi", end="")
        case 5:
          print("Beshinchi", end="")
        case 6:
          print("Oltinchi", end="")
        case 7:
          print("Yettinchi", end="")
        case 8:
          print("Sakkizinchi", end="")
        case 9:
          print("To'qqizinchi", end="")
    match b:
          case 4:
            print(" Aprel.")
          case 6:
            print(" Iyun.")
          case 9:
            print(" Sentabr.")
          case 11:
            print(" Noyabr.")
  elif a == 30 or a == 20 or a == 10:
    match onliklar:
          case 1:
            print("O'ninchi ", end="")
          case 2:
            print("Yigirmanchi ", end="")
          case 3:
            print("O'ttizinchi ", end="")
    match b:
          case 4:
            print(" Aprel.")
          case 6:
            print(" Iyun.")
          case 9:
            print(" Sentabr.")
          case 11:
            print(" Noyabr.")
  
  
  # 31 Yanvar Mart May Iyul Avgust Oktabr Dekabr
  # 30 Aprel Iyun Sentabr Noyabr 
  # 29 Fevral
elif (b <= 12 and b >= 1) and (a >= 1 and a <= 31):
  if not( a == 10 or a == 20 or a == 30):
    match onliklar:
          case 1:
            print("O'n ", end="")
          case 2:
            print("Yigirma ", end="")
          case 3:
            print("O'ttiz ", end="")
    match birliklar:
        case 1:
          print("Birinchi", end="")
        case 2:
          print("Ikkinchi", end="")
        case 3:
          print("Uchinchi", end="")
        case 4:
          print("To'rtinchi", end="")
        case 5:
          print("Beshinchi", end="")
        case 6:
          print("Oltinchi", end="")
        case 7:
          print("Yettinchi", end="")
        case 8:
          print("Sakkizinchi", end="")
        case 9:
          print("To'qqizinchi", end="")
    match b:
        case 1:
          print(" Yanvar.")
        case 2:
          print(" Fevral.")
        case 3:
          print(" Mart.")
        case 5:
          print(" May.")
        case 7:
          print(" Iyul.")
        case 8:
          print(" Avgust.")
        case 10:
          print(" Oktabr.")
        case 12:
          print(" Dekabr.")
  elif a == 30 or a == 20 or a == 10:
    match onliklar:
      case 1:
        print("O'ninchi ", end="")
      case 2:
        print("Yigirmanchi ", end="")
      case 3:
        print("O'ttizinchi ", end="")
    match b:
      case 1:
        print(" Yanvar.")
      case 2:
        print(" Fevral.")
      case 3:
        print(" Mart.")
      case 5:
        print(" May.")
      case 7:
        print(" Iyul.")
      case 8:
        print(" Avgust.")
      case 10:
        print(" Oktabr.")
      case 12:
        print(" Dekabr.")
elif b <= 0:
  print("Boshqattan urinib ko'ring! Oylar faqat 1 va 12 tartib raqamlari orasida bo'lishi mumkin.")
elif a > 31:
    print("Boshqattan urinib ko'ring! Bu oy 31 kundan ortiq bo'la olmaydi.")
else:
   print("Boshqattan urinib ko'ring! Hech qaysi bir yil 12 oydan ortiq bo'la olmaydi.")
  