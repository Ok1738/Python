M = int(input("Karataning (1 - g'isht, 2 - olma, 3 - chillak, 4 - qarg'a) turlari bor."
                "Tanlang: "))
N = int(input("Kartaning (6, 7, 8, 9, 10, 11 - Valet, 12 - Dama, 13 - Qirol, 14 - Tuz) qiymatlari bor."
              "Tanlang: "))
if N >= 6 and N <= 14:
  match N:
    case 6:
      print("Olti ", end="")
    case 7:
      print("Yetti ", end="")
    case 8:
      print("Sakkiz ", end="")
    case 9:
      print("To'qqiz ", end="")
    case 10:
      print("O'n ", end="")
    case 11:
      print("Valet ", end="")
    case 12:
      print("Dama ", end="")
    case 13:
      print("Qirol ", end="")
    case 14:
      print("Tuz ", end="")
else:
  print("Karta faqat 6 va 14 oralig'ida bo'ladi. Boshqattan urinib ko'ring!")
if M >= 1 and M <= 4:
  match M:
    case 1:
      print("g'isht.")
    case 2:
      print("olma.")
    case 3:
      print(" chillak.")
    case 4:
      print("qarg'a.")
else:
  print("Karta turi 1 va 4 oralig'ida bo'lishi kerak.")
